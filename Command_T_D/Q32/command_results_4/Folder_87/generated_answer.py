import re

def insert_after_character(text):
    return re.sub('m', 'mN', text)