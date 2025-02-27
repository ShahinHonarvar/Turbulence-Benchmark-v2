def insert_before_character(s):
    return ''.join(('K' + char if char == ' ' else char for char in s))