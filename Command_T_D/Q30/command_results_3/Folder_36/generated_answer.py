import re

def insert_before_character(text):
    return re.sub('(?<=A)H', 'H\\1', text)