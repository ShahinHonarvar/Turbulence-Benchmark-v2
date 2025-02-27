import re

def insert_before_character(string):
    return re.sub('(C)', 'Z\\1', string)