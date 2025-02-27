import re

def insert_before_character(text):
    return re.sub('a(?!0)', '0a', text)