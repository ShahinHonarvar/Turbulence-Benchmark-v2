def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[331:713] if 'M' < char < '_']
    return ''.join([char for char in input_string if char not in chars_to_remove])