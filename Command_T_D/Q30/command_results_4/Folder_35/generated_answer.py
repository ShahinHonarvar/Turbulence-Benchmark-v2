import re

def insert_before_character(string):
    return re.sub('(?<=9)9', '9M', string)