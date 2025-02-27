def insert_before_character(s):
    return ''.join(('W' + char if char == ' ' else char for char in s))