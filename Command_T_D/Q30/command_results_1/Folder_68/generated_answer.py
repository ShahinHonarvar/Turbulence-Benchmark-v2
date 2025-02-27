import re

def insert_before_character(string):
    return re.sub('(?i)i', '0\\i', string)