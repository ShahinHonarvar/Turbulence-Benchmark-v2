def insert_after_character(str):
    return ''.join([char + 'U' if char == 'u' else char for char in str])