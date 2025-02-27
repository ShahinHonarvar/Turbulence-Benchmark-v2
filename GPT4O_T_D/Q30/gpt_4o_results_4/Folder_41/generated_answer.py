def insert_before_character(s):
    return ''.join(('oO' if char == 'O' else char for char in s))