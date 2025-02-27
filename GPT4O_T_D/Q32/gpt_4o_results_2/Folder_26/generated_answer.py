def insert_after_character(s):
    return ''.join(('rw' if char == 'r' else char for char in s))