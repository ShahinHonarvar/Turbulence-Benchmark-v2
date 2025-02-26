def insert_before_character(input_string):
    return ''.join(['h' + char if char == '9' else char for char in input_string])