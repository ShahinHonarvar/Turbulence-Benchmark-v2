import re

def insert_after_character(string):
    return re.sub('(?<=i)i', 'ii', string)