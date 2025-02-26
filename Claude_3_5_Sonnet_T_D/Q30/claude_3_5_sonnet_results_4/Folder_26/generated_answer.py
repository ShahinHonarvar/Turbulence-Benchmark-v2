def insert_before_character(input_string):
    return ''.join(['w' + char if char == 'r' else char for char in input_string])