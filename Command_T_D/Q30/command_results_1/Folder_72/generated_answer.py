import re

def insert_before_character(s):
    return re.sub('O(?!d)', 'Od', s)