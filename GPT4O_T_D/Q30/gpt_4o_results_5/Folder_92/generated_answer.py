def insert_before_character(s):
    return ''.join(('aa' if char == 'a' else char for char in s))