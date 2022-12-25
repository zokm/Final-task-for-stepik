# данный файл создан для селекторов, чтобы они находились в одном месте и проще было их изменять
# (поменял в одном месте и не надо искать покоду повторяющиеся селекторы)

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:

