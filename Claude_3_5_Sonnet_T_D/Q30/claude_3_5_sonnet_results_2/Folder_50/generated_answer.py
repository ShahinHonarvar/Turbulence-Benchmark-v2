def insert_before_character(input_string):
    return ''.join(['u' + char if char == 't' else char for char in input_string])