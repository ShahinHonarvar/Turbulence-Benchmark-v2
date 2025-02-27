def insert_before_character(s):
    return ''.join(('E' + char if char == 'e' else char for char in s))