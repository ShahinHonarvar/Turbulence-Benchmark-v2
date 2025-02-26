def insert_before_character(input_string):
    return ''.join(['R' + char if char == '5' else char for char in input_string])