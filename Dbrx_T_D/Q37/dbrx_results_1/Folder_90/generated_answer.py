def filter_chars(input_string):
    return ''.join([char for char in input_string if not (348 <= input_string.index(char) <= 852 and 'J' <= char <= 'b')])