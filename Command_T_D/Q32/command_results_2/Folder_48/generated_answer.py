import re

def insert_after_character(string):
    return re.sub('S(?!U)', 'SU', string)