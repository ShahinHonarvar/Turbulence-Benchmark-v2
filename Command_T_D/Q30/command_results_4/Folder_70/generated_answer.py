import re

def insert_before_character(text):
    return re.sub('(P)', 'V\\1', text)