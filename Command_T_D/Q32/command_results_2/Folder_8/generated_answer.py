import re

def insert_after_character(string):
    return re.sub('(E)(?=T)', '1T', string)