import re

def insert_after_character(text):
    return re.sub('(.)P', '1PP', text)