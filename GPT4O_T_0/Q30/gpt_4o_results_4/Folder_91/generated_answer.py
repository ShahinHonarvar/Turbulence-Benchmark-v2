def insert_before_character(s):
    return ''.join(('0a' if char == 'a' else char for char in s))