def insert_before_character(input_string):
    return 'M'.join(('g' if i % 2 == 0 else x for i, x in enumerate(input_string)))