def filter_chars(input_string):
    chars_to_remove = [c for c in input_string[4:5] if 'Y' < c < 's']
    return ''.join((c for c in input_string if c not in chars_to_remove))