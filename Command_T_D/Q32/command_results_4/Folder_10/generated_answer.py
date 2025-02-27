import re

def insert_after_character(string):
    return re.sub('(j)', 'v1', string)