def insert_before_character(s):
    return ''.join(('sH' if char == 'H' else char for char in s))