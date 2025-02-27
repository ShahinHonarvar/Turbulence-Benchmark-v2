def insert_before_character(s):
    return ''.join(('nH' if char == 'H' else char for char in s))