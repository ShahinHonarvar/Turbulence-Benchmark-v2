def insert_after_character(s):
    return ''.join([char + '6' if char == 'a' else char for char in s])