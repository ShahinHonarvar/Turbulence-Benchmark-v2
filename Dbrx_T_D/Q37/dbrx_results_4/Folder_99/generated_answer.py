def filter_chars(input_string):
    return ''.join([char for char in input_string if not (373 <= input_string.index(char) <= 901 and 'T' <= char <= 'h')])