def insert_after_character(input_string):
    return ''.join(('G' if c == 't' else c for c in input_string)) + 'G' if input_string.endswith('t') else ''