import re

def insert_before_character(text):
    return re.sub('(?<=.)H', 'H\\1', text)