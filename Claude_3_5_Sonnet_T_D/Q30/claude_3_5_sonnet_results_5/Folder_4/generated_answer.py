def insert_before_character(input_string):
    return ''.join(['6' + char if char == 'a' else char for char in input_string])