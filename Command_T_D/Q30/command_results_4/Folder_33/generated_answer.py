import re

def insert_before_character(text):
    return re.sub('(?<=a)n', 'n', text)