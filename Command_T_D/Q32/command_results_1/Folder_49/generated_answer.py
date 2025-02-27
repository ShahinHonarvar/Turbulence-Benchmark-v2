import re

def insert_after_character(text):
    return re.sub('(i)', '1i', text)