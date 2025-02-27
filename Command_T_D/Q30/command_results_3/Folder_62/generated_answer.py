import re

def insert_before_character(string):
    return re.sub('(\\.)o', '\\1o\\1', string)