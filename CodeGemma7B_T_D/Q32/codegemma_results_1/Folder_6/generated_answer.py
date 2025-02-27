def insert_after_character(str):
    return ''.join([char + 'u' if char == 'X' else char for char in str])