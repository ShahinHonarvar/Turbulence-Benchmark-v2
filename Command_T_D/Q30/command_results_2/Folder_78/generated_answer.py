import re

def insert_before_character(text):
    return re.sub('(H)(?=\\s)', '\\1s\\2', text)