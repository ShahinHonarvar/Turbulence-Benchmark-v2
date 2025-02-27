import re

def insert_before_character(text):
    return re.sub('(.)H', '\\1\\H', text)