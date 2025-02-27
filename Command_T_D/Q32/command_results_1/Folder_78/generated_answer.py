import re

def insert_after_character(text):
    return re.sub('(?i)H(?!s)', 'H1s', text)