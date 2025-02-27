import re

def insert_before_character(string):
    return re.sub('U', 'U\\1', string)