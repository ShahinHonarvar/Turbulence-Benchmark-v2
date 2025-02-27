import re

def insert_before_character(s):
    return re.sub('(P)', '(V\\1)', s)