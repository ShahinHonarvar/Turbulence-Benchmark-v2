def filter_chars(input_string):
    return ''.join([char for char in input_string if not (477 <= input_string.index(char) <= 984 and ',' <= char <= 'V')])