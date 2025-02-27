import re

def insert_before_character(string):
    return re.sub('(e)', '0\\1', string)