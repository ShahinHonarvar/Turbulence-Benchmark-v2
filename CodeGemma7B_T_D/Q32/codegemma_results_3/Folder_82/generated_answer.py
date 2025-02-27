from re import sub

def insert_after_character(a):
    return sub('(I+)', '\\\\1I', a)