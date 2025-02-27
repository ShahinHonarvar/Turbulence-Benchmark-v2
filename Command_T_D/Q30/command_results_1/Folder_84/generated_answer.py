import re

def insert_before_character(text):
    return re.sub('H', 'nH', text)