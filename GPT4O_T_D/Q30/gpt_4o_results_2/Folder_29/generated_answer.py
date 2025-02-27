def insert_before_character(s):
    return ''.join(('zN' if char == 'N' else char for char in s))