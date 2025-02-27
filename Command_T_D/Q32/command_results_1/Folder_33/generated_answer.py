import re

def insert_after_character(text):
    return re.sub('a(?!n)', 'an', text)