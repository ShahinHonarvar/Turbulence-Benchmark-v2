import re

def insert_after_character(text):
    return re.sub('(E)f', '1f', text)