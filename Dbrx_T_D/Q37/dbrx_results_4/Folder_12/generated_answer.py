def filter_chars(input_string):
    filtered_chars = [char for char in input_string[19:91] if not 'F' <= char <= 'h']
    return ''.join(filtered_chars)