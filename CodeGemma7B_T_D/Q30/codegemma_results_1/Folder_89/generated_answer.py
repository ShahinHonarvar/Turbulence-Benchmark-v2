def insert_before_character(s):
    return ''.join([char if char != ' ' else 'W' + char for char in s])