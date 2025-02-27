def insert_after_character(input_string):
    return ''.join((char + 'Q' if char == 'm' else char for char in input_string))