import re

def insert_after_character(text):
    return re.sub('(?<=F)u', 'u', text)