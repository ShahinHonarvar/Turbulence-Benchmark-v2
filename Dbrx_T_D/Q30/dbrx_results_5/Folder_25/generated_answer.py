def insert_before_character(input_string):
    return ''.join(['W' + char if char == 'e' else char for char in input_string])