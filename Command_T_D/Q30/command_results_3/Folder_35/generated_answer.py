import re

def insert_before_character(text):
    return re.sub('9', '\\1M\\1', text)