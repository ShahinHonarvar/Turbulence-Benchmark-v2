def insert_before_character(input_string):
    return ''.join(['G' + char if char == 'c' else char for char in input_string])