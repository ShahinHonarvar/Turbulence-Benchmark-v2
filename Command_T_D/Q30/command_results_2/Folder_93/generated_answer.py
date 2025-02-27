import re

def insert_before_character(text):
    return re.sub('(Y)', '\\1\\4', text)