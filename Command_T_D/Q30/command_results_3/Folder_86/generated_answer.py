import re

def insert_before_character(string):
    return re.sub('O', 'Q\\O', string)