import re

def insert_before_character(text):
    return re.sub('(i)', '\\1I', text)