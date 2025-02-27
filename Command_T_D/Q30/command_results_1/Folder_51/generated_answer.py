import re

def insert_before_character(text):
    return re.sub('o', 'O\\1', text)