def insert_before_character(str):
    return ''.join([char + 't' if char == 'a' else char for char in str])