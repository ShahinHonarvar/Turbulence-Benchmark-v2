import re

def insert_before_character(string):
    return re.sub('6', '9\\6', string)