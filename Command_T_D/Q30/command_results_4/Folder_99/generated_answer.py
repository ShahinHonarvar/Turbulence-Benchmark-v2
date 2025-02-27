import re

def insert_before_character(text):
    return re.sub('(a)', 'W\\1', text)