import re

def insert_after_character(string):
    return re.sub('(E)', 'TE', string)