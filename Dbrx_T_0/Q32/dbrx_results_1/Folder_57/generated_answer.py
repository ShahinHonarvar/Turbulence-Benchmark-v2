def insert_after_character(input_string):
    return input_string.replace('s', 'sw', 1) if input_string.count('s') else input_string