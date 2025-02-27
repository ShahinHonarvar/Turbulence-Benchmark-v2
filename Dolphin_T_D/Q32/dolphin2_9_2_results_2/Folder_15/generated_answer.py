def insert_after_character(input_string):
    return 'o'.join(('o' if character == 'o' else character for character in input_string))