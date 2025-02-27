def insert_after_character(s):
    return ''.join((char + 'O' if char == 'O' else char for char in s))