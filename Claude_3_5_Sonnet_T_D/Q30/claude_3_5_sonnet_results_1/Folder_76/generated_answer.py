def insert_before_character(input_string):
    return ''.join(['m' + char if char == 'F' else char for char in input_string])