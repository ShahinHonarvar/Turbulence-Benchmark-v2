import re

def insert_after_character(string):
    return re.sub('Q(?!I)', 'QI', string)