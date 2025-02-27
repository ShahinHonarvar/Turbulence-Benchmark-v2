def insert_before_character(s):
    return ''.join(('dO' if char == 'O' else char for char in s))