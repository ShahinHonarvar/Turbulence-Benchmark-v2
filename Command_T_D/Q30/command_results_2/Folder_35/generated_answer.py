import re

def insert_before_character(s):
    return re.sub('9', 'M\\9', s)