def insert_after_character(s):
    return ''.join(('AA' if char == 'A' else char for char in s))