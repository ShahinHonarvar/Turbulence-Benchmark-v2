def insert_before_character(input_string):
    return 'H'.join(('C' if char == 'C' else '' for char in input_string))