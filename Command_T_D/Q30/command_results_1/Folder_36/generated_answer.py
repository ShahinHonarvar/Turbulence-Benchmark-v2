import re

def insert_before_character(s):
    return re.sub('A(?!H)', 'AH', s)