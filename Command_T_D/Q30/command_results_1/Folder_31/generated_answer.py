import re

def insert_before_character(s):
    return re.sub('(?<=B)N', 'N', s)