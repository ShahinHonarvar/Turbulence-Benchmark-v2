import re

def insert_before_character(string):
    return re.sub('(C)', 'P\\1', string)