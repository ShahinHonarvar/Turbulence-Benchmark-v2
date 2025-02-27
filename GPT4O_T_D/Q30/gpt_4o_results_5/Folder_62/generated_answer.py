def insert_before_character(s):
    return ''.join(('o ' if char == ' ' else char for char in s))