import re

def insert_before_character(text):
    return re.sub('(.)\\sP', '\\1\\sP', text)