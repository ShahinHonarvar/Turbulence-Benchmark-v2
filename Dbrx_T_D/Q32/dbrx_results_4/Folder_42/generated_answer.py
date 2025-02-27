def insert_after_character(s):
    return ''.join((char if char != 'O' else 'Oj' for char in s))