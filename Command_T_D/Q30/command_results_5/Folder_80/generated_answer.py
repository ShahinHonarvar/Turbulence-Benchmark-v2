import re

def insert_before_character(string):
    return re.sub('(.*)\\sX', '\\1\\sXX', string)