import re

def insert_before_character(string):
    return re.sub('(?!z)N', 'z\\1', string)