def insert_after_character(s):
    return ''.join([char + '6' if char == 'X' else char for char in s])