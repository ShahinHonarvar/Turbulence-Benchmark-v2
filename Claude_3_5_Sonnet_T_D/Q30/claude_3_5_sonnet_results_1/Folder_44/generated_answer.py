def insert_before_character(input_string):
    return ''.join(['M' + char if char == 'g' else char for char in input_string])