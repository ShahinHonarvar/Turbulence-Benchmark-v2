def insert_before_character(s):
    return ''.join(('ZC' if char == 'C' else char for char in s))