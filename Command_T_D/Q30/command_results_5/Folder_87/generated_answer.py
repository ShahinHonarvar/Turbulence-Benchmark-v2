import re

def insert_before_character(text):
    return re.sub('m', 'N\\1', text)