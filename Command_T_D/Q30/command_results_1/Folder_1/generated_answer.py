import re

def insert_before_character(text):
    return re.sub('U', 'T\x01', text)