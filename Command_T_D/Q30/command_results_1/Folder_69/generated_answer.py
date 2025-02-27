import re

def insert_before_character(text):
    return re.sub('(.)P', '\\1\\p', text)