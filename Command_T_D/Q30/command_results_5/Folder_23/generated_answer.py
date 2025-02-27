import re

def insert_before_character(s):
    return re.sub('b(?!y)', 'by', s)