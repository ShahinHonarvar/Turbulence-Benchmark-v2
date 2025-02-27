import re

def insert_before_character(text):
    return re.sub('u', 'u\\u', text)