def insert_before_character(input_string):
    return ''.join(['4' + char if char == 'Y' else char for char in input_string])