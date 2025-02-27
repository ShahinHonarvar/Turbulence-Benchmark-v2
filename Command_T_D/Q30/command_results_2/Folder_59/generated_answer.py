import re

def insert_before_character(string):
    return re.sub('o', '0o', string)