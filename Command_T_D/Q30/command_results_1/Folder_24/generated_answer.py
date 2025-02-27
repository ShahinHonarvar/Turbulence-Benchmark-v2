import re

def insert_before_character(string):
    return re.sub('0', '4\\0', string)