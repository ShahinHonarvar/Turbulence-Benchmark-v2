import re

def insert_after_character(text):
    return re.sub('b0b', '0H', text)