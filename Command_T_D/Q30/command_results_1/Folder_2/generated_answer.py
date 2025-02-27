import re

def insert_before_character(text):
    return re.sub('(C)', 'Z\\1', text)