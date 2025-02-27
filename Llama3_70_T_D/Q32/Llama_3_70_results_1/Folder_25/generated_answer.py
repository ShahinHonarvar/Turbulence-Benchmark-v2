def insert_after_character(input_string):
    return ''.join(('W' + c if c == 'e' else c for c in input_string))