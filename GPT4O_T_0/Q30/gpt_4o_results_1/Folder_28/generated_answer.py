def insert_before_character(s):
    return ''.join(('1r' if char == 'r' else char for char in s))