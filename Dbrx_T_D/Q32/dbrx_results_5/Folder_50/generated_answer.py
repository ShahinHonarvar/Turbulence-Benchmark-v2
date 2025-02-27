def insert_after_character(input_string):
    return input_string.replace('t', 'tu', 1) if input_string.startswith('t') else 't' + input_string.replace('t', 'tu', 1)