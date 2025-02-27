def insert_after_character(input_string):
    return ''.join((c + '0' if c == 'o' else c for c in input_string))