def insert_after_character(input_string):
    return ''.join([char + 'W' if char == ' ' else char for char in input_string])