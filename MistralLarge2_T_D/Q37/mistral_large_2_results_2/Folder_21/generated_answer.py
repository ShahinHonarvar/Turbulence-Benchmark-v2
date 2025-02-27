def filter_chars(input_string):
    indices_range = range(603, 760)
    target_chars = [char for idx, char in enumerate(input_string) if idx in indices_range and 'Q' <= char <= 'h']
    for char in target_chars:
        input_string = input_string.replace(char, '')
    return input_string