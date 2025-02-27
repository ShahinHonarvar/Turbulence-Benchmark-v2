import re

def insert_after_character(string):
    return re.sub('6(?!9)', '69', string)