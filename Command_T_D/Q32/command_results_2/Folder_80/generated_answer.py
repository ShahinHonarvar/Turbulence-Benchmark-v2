import re

def insert_after_character(text):
    return re.sub('.', 'X1', text)