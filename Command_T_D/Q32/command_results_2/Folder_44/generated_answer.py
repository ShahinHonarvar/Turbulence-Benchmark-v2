import re

def insert_after_character(s):
    return re.sub('g(?!M)', 'Mg', s)