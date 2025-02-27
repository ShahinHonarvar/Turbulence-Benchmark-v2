import re

def insert_before_character(text):
    return re.sub('(C)', 'H\\1', text)