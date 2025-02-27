def insert_before_character(s):
    return ''.join(['UU' if char == 'U' else char for char in s])