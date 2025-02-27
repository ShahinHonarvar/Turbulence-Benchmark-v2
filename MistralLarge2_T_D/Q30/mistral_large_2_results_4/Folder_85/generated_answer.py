def insert_before_character(s):
    return ''.join(('a' + char if char == 'o' else char for char in s))