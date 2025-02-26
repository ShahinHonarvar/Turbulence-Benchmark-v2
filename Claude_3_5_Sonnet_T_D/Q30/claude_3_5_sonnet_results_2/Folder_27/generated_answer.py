def insert_before_character(input_string):
    return ''.join(['j' + char if char == 'N' else char for char in input_string])