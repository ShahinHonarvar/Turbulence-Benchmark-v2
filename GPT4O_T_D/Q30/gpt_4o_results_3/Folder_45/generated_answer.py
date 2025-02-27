def insert_before_character(s):
    return ''.join(('O' + char if char == 'O' else char for char in s))