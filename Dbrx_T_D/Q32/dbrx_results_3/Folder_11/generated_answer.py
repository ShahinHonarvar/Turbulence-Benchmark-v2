def insert_after_character(input_string):
    return input_string.replace('g', 'gt', 1) if input_string.count('g') else input_string