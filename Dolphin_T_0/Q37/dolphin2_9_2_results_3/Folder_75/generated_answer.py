def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[34:68] if 'W' <= char <= 'x']
    return ''.join(list(filter(lambda char: char not in chars_to_remove, input_string)))