import re

def insert_after_character(string):
    return re.sub('(?<=T)V', 'V', string)