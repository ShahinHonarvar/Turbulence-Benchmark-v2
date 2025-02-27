import re

def insert_after_character(string):
    return re.sub('(?<=H)n', 'n', string)