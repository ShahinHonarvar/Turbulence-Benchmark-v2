import re

def insert_before_character(text):
    return re.sub('(.)K', '\\1K', text)