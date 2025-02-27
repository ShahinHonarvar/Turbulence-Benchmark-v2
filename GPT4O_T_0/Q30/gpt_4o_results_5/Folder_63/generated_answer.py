def insert_before_character(s):
    return ''.join(('R5' if char == '5' else char for char in s))