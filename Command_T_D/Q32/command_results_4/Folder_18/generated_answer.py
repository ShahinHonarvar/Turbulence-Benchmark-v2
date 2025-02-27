import re

def insert_after_character(string):
    return re.sub('K(?!l)', 'KL', string)