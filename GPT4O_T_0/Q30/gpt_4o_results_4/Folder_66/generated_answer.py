def insert_before_character(s):
    return ''.join(('k' + char if char == 'k' else char for char in s))