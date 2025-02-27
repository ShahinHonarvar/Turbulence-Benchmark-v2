import re

def insert_before_character(string):
    return re.sub('(?<=E)T', 'T\\1', string)