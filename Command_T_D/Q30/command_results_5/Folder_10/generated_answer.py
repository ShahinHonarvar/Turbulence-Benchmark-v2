import re

def insert_before_character(string):
    return re.sub('(j)', '\\1v', string)