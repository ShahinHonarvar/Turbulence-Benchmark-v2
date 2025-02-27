def insert_before_character(s):
    return ''.join(('0i' if char == 'i' else char for char in s))