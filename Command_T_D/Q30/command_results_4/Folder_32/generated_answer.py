import re

def insert_before_character(string):
    return re.sub('(F)', '\\1u', string)