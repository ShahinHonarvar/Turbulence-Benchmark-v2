def filter_chars(input_string):
    chars_to_remove = {c for c in input_string[31:73] if 'M' < c < 'j'}
    return ''.join((c for c in input_string if c not in chars_to_remove))