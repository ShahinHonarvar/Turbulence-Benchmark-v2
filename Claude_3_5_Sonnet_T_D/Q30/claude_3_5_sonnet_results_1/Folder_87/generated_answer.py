def insert_before_character(input_string):
    return ''.join(['N' + char if char == 'm' else char for char in input_string])