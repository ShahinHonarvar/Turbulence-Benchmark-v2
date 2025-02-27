def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[3:5] if 'Y' < char < 's']
    return ''.join([c for c in input_string if c not in chars_to_remove])