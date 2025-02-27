import re

def insert_after_character(s):
    return re.sub('b(?!y)', 'by', s)