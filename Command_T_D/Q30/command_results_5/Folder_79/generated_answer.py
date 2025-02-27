import re

def insert_before_character(text):
    return re.sub('(E)', 'E\\1', text)