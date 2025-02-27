def insert_before_character(s):
    return ''.join((char if char != 'U' else 'TU' for char in s))