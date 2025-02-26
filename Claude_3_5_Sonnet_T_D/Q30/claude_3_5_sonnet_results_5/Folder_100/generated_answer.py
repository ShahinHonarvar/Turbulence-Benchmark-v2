def insert_before_character(input_string):
    return ''.join([' ' + char if char == '0' else char for char in input_string])