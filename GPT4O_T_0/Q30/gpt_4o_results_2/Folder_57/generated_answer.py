def insert_before_character(s):
    return ''.join(('w' + char if char == 's' else char for char in s))