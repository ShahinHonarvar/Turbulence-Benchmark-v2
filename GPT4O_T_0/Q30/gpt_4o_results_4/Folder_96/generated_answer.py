def insert_before_character(s):
    return ''.join(('A' + char if char == 'a' else char for char in s))