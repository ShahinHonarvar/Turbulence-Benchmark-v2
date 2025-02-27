def filter_chars(input_string):
    filtered_chars = [char for char in input_string if 88 <= input_string.index(char) <= 90 and 'J' <= char <= 'Q']
    return ''.join((char for char in input_string if char not in filtered_chars))