def insert_before_character(s):
    return ''.join(('0o' if char == 'o' else char for char in s))