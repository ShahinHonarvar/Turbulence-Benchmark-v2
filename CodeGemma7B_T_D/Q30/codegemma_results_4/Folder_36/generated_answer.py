def insert_before_character(input_string):
    return ''.join([char + 'H' if char == 'A' else char for char in input_string])