def insert_before_character(input_string):
    return ''.join(['E' if i + 1 < len(input_string) and input_string[i + 1] == 'e' else c for i, c in enumerate(input_string)])