def filter_chars(input_string):
    chars_to_remove = [c for c in input_string[2:7] if '-' < c < 'L']
    return ''.join((c for c in input_string if c not in chars_to_remove))