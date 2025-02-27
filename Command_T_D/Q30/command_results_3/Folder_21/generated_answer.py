import re

def insert_before_character(string):
    return re.sub('(.)\\sK', '\\1K', string)