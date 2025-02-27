def insert_before_character(s):
    return ''.join(('T' + char if char == 'U' else char for char in s))