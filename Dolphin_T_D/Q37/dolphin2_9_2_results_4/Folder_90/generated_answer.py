def filter_chars(string):
    chars_to_remove = [char for char in string[348:853] if 'J' <= char <= 'b']
    return ''.join([char for char in string if char not in chars_to_remove])