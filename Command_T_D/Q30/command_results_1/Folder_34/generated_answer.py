import re

def insert_before_character(s):
    return re.sub('A(?!a)', 'Aa', s)