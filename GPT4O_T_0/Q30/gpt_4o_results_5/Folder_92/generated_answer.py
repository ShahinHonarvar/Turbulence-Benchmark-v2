def insert_before_character(s):
    return ''.join(('a' + char if char == 'a' else char for char in s))