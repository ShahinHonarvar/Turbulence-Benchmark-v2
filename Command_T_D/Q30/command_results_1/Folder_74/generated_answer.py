import re

def insert_before_character(text):
    return re.sub('(?! )T', '\\1 \\2', text)