import re

def insert_after_character(text):
    return re.sub('(?<=9)M', 'M', text)