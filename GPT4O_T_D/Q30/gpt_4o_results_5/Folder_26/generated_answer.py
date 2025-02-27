def insert_before_character(s):
    return ''.join(('w' + char if char == 'r' else char for char in s))