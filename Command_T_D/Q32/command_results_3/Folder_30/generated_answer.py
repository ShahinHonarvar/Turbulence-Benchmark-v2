import re

def insert_after_character(string):
    return re.sub('4(?!F)', '4F', string)