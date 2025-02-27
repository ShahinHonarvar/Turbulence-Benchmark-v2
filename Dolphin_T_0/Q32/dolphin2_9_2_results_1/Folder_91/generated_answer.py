def insert_after_character(input_string):
    return '0'.join([char if char != 'a' else 'a0' for char in input_string])