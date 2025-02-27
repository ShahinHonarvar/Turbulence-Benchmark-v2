import re

def insert_after_character(text):
    return re.sub('U', 'U1', text)