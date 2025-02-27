def insert_before_character(str):
    return ''.join([char + 'K' if char == ' ' else char for char in str])