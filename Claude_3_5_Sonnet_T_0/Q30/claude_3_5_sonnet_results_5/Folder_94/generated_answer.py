def insert_before_character(input_string):
    return ''.join(['5' + char if char == ' ' else char for char in input_string])