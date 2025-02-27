def insert_after_character(s):
    return ''.join(('Aa' if char == 'A' else char for char in s))