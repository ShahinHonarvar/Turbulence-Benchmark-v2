import re

def insert_after_character(str):
    return re.sub('u', 'Uu', str)