def filter_chars(input_string):
    chars_to_remove = {char for idx, char in enumerate(input_string) if 12 <= idx <= 88 and '&' <= char <= 'v'}
    return ''.join((char for char in input_string if char not in chars_to_remove))