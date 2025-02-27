def insert_after_character(str):
    return ''.join([char + 'A' if char == 'A' else char for char in str])