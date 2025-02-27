def insert_before_character(s):
    return ''.join(('y' + char if char == 'b' else char for char in s))