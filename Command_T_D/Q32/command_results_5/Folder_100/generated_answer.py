import re

def insert_after_character(string):
    return re.sub('0', '0 0', string)