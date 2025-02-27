def insert_before_character(input_string):
    return 'T'.join(('E' if char == 'E' else char for char in input_string))