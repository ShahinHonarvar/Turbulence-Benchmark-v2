import re

def insert_after_character(text):
    pattern = 'w'
    replacement = 'w\\\n'
    return re.sub(pattern, replacement, text)