import re

def insert_before_character(s):
    return re.sub('(?!z)N', 'zN', s)