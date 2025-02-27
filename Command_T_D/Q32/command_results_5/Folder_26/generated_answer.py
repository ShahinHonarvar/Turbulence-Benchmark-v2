import re

def insert_after_character(text):
    return re.sub('r(?!w)', 'r1w', text)