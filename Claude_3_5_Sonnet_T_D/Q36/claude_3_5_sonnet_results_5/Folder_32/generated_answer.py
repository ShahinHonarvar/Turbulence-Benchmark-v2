def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[41:63] if '7' < c < 'H'))
    return ''.join((c for c in input_string if c not in chars_to_remove))