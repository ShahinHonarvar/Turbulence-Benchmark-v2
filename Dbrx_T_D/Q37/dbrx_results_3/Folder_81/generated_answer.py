def filter_chars(input_string):
    filtered_string = ''.join([char for char in input_string if not (19 <= input_string.index(char) <= 92 and '8' <= char <= 'm')])
    return filtered_string