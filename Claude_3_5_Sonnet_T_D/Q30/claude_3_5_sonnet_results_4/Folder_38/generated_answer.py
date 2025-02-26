def insert_before_character(input_string):
    return ''.join(['6' + char if char == 'X' else char for char in input_string])