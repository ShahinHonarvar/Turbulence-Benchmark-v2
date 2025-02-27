import re

def insert_before_character(text):
    return re.sub('(F)', '\\1o\\1', text)