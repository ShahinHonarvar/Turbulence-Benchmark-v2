def insert_after_character(s):
    return ''.join([char + 'w' if char == 's' else char for char in s])