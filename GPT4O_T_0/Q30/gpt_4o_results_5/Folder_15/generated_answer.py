def insert_before_character(s):
    return ''.join(('o' + char if char == 'o' else char for char in s))