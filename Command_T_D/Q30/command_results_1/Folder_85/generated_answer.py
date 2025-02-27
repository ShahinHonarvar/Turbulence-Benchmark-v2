import re

def insert_before_character(text):
    return re.sub('o', 'a\\1', text)