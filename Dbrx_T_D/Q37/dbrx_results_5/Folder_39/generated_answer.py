def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[52:82] if 'A' <= char <= 'U']
    result = [char for char in input_string if char not in chars_to_remove]
    return ''.join(result)