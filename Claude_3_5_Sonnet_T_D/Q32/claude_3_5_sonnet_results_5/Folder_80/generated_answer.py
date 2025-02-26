def insert_after_character(s):
    return ''.join([char + 'X' if char == ' ' else char for char in s])