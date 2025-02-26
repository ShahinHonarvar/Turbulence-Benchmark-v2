def insert_before_character(input_string):
    return ''.join(['1' + char if char == 'j' else char for char in input_string])