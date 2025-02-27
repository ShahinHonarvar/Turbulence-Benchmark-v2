def insert_after_character(s):
    return ''.join([char + 'A' if char == 'a' else char for char in s])