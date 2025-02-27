def insert_before_character(s):
    return ''.join(('aU' if char == 'U' else char for char in s))