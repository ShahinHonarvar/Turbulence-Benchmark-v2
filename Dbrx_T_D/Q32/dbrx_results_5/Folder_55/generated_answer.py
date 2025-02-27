def insert_after_character(input_string):
    return input_string.replace('u', 'uU', 1).replace('U', 'uU') if 'u' in input_string else input_string