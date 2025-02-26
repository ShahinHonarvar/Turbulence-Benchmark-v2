def insert_after_character(input_string):
    return ''.join([char + 'o' if char == ' ' else char for char in input_string])