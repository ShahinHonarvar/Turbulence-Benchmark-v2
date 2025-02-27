def filter_chars(input_string):
    if len(input_string) <= 40:
        return input_string
    chars_to_remove = {char for char in input_string[35:41] if ')' <= char <= 'l'}
    return ''.join((char for char in input_string if char not in chars_to_remove))