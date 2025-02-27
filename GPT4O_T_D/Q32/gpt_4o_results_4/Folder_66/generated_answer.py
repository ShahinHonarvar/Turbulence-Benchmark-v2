def insert_after_character(s):
    return ''.join([char + 'k' if char == 'k' else char for char in s])