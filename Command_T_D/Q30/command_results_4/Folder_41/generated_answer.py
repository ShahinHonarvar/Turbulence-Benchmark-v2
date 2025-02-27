import re

def insert_before_character(text):
    return re.sub('O', 'o\\1', text)