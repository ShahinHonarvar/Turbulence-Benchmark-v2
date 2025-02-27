def insert_before_character(s):
    return ''.join(('U' + char if char == 'S' else char for char in s))