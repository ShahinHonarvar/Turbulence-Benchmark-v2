import re

def insert_after_character(string):
    return re.sub('a(?!a)', 'aa', string)