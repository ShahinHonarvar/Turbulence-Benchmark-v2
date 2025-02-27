def insert_before_character(s):
    return ''.join(('0e' if char == 'e' else char for char in s))