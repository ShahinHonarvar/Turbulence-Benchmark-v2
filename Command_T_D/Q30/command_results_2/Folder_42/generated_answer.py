import re

def insert_before_character(s):
    return re.sub('O(?!j)', 'Oj', s)