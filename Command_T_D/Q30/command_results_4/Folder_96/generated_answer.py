import re

def insert_before_character(text):
    return re.sub('a', 'A\\1', text)