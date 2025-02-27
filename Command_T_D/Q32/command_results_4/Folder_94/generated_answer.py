import re

def insert_after_character(string):
    return re.sub('(.)5', '15', string)