def insert_after_character(s):
    return ''.join([char + 'P' if char == 'C' else char for char in s])