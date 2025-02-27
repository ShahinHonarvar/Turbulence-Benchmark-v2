import re

def insert_before_character(text):
    return re.sub('g(?!t)', 'gt', text)