def insert_before_character(input_string):
    return ''.join(('0' + char if char == 'o' else char for char in input_string))