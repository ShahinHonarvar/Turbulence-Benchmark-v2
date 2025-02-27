def insert_after_character(input_str):
    return ''.join([c + '0' if c == 'i' else c for c in input_str])