def insert_before_character(input_str):
    return ''.join(['j' if char == 'O' else char for char in input_str])