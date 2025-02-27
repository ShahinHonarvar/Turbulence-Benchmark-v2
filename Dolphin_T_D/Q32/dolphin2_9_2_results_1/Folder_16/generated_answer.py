def insert_after_character(input_string):
    return ''.join(('n' if i > 0 and input_string[i - 1] == 'w' else c for i, c in enumerate(input_string)))