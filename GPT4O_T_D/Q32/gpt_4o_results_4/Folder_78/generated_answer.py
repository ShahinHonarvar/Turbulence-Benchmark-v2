def insert_after_character(input_string):
    return ''.join((char + 's' if char == 'H' else char for char in input_string))