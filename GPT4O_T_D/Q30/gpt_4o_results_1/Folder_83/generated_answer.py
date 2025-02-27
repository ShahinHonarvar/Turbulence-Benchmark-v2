def insert_before_character(s):
    return ''.join(('eE' if char == 'E' else char for char in s))