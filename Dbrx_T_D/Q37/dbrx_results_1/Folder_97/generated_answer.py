def filter_chars(input_string):
    filtered_chars = [char for char in input_string if 227 <= input_string.index(char) <= 235 and 'D' <= char <= 'u']
    return ''.join(filtered_chars)