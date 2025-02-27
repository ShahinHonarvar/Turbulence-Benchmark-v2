import re

def insert_before_character(string):
    return re.sub('(?<=.)H', 'H\\1', string)