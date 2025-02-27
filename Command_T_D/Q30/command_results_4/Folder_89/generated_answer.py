import re

def insert_before_character(text):
    return re.sub('(.)W', '\\1\\W', text)