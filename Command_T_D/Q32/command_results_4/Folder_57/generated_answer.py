import re

def insert_after_character(text):
    return re.sub('sw+', 'sww+', text)