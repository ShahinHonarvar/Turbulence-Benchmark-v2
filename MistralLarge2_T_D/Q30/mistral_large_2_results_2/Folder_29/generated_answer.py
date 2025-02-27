def insert_before_character(s):
    return ''.join([char + 'z' if char == 'N' else char for char in s])