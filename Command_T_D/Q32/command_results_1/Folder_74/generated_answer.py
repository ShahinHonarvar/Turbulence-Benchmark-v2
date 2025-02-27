import re

def insert_after_character(string):
    return re.sub('(T)s', '1T 2s', string)