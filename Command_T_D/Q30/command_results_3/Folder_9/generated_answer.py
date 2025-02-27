import re

def insert_before_character(string):
    return re.sub('(e)', 'E\\1', string)