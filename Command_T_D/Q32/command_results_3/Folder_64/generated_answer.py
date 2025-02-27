import re

def insert_after_character(string):
    return re.sub('(u)', '1u', string)