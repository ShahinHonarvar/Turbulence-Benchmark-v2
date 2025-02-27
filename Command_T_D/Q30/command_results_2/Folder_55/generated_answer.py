import re

def insert_before_character(text):
    return re.sub('u', 'U\\1', text)