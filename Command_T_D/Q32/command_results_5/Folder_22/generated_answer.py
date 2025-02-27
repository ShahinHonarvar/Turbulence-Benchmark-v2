import re

def insert_after_character(s):
    return re.sub('U(?!U)U', 'UU', s)