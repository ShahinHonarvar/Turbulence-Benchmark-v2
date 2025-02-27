import re

def insert_after_character(string):
    return re.sub('(.)H', '1H1', string)