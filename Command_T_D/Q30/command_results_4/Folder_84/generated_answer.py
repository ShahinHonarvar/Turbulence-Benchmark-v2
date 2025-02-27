import re

def insert_before_character(text):
    return re.sub('(H)(?=.)', '\\1n', text)