def insert_after_character(input_string):
    return ''.join((char + 'w' if char == 's' else char for char in input_string))