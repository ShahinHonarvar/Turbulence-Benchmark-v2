import re

def insert_before_character(s):
    return re.sub('A(?!A)', 'AA', s)