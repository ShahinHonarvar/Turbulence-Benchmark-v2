def insert_before_character(input_string):
    return ''.join(['o' + char if char == 'F' else char for char in input_string])