def insert_before_character(input_string):
    return ''.join(['a' + char if char == 'U' else char for char in input_string])