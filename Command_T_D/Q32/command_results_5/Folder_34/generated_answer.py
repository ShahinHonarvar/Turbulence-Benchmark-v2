import re

def insert_after_character(text):
    return re.sub('A(?!a)', 'A1a', text)