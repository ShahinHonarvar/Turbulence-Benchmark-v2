import re

def insert_before_character(string):
    return re.sub('(R)', '\\1V', string)