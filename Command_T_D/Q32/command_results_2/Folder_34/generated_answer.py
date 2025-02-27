import re

def insert_after_character(string):
    return re.sub('(A)', 'a1', string)