import re

def insert_after_character(s):
    return re.sub('A(?!H)', 'AH', s)