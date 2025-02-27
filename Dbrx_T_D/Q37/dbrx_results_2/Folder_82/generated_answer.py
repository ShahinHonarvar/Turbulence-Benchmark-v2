def filter_chars(input_string):
    filtered_chars = [char for char in input_string if not (12 <= input_string.index(char) <= 25 and 'P' <= char <= 'x')]
    return ''.join(filtered_chars)