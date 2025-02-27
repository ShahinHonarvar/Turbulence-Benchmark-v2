import re

def insert_before_character(s):
    return re.sub('(?<=2)S', 'S', s)