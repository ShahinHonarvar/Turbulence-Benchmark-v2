from re import sub

def insert_before_character(string):
    pattern = '(F)'
    replacement = 'm\\\\1'
    return sub(pattern, replacement, string)