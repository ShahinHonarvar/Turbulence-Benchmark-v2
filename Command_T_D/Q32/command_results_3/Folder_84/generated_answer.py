import re

def insert_after_character(text):
    return re.sub('(?<=H)n', '1', text)