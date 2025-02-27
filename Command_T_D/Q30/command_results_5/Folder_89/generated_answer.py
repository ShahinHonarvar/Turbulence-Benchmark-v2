import re

def insert_before_character(text):
    return re.sub('(.)W', '\\1W', text)