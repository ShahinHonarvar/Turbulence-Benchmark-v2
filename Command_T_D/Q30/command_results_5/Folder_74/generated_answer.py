import re

def insert_before_character(s):
    return re.sub('(?! )T', '\\1T ', s)