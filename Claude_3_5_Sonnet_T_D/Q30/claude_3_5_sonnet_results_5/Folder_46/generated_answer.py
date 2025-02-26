def insert_before_character(input_string):
    return ''.join(['W' + char if char == '6' else char for char in input_string])