def insert_after_character(input_string):
    return input_string.replace('t', 'tu', 1) if input_string[0] != 't' else 'u' + input_string.replace('t', 'tu', 1)