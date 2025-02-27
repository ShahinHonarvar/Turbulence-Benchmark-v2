def insert_before_character(s):
    return ''.join(['X' + char if char == ' ' else char for char in s])