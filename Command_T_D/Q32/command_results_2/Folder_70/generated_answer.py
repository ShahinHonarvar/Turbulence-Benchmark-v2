import re

def insert_after_character(string):
    return re.sub('(P)(?!V)', 'PV', string)