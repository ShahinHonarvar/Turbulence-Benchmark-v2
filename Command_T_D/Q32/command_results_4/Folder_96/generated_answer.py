import re

def insert_after_character(s):
    return re.sub('a(?!A)', 'aa', s)