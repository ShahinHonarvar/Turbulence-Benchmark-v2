def insert_before_character(input_string):
    return 'H'.join(('C' if c == 'C' else c for c in input_string))