import re

def insert_after_character(text):
    return re.sub('bNb(?!z)', '1z', text)