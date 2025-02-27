def insert_before_character(str):
    return ''.join([char + 's' if char == 'H' else char for char in str])