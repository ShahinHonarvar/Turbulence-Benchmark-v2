import re

def insert_before_character(string):
    return re.sub('(^|.*\\b)w', '\\1n\\1w', string)