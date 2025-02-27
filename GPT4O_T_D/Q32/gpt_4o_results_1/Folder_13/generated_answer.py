def insert_after_character(s):
    return ''.join((char + 'N' if char == 'x' else char for char in s))