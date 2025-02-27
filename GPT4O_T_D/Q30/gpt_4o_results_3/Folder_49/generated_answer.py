def insert_before_character(s):
    return ''.join(('ii' if char == 'i' else char for char in s))