def insert_before_character(input_string):
    return ''.join(['n' + char if char == 'w' else char for char in input_string])