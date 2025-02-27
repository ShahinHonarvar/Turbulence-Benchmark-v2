import re

def insert_before_character(string):
    return re.sub('(^.)w', '\\1wn', string)