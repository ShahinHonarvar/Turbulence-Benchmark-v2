import re

def insert_before_character(text):
    return re.sub('(.)\\s', '\\1P\\s', text)