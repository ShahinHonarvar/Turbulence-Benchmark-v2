def insert_before_character(s):
    return ''.join(('ho' if char == 'o' else char for char in s))