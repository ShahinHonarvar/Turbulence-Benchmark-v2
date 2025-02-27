import re

def insert_after_character(s):
    return re.sub('a(?!t)', 'at', s)