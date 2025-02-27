import re

def insert_before_character(text):
    return re.sub('r', 'w\\1', text)