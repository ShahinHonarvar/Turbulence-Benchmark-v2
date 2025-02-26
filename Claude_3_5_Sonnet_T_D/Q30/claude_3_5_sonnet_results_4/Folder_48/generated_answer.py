def insert_before_character(input_string):
    return ''.join(['U' + char if char == 'S' else char for char in input_string])