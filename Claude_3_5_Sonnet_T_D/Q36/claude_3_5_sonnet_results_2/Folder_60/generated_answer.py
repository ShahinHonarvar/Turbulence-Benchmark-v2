def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[24:83] if 'f' < c < 'o'))
    return ''.join((c for c in input_string if c not in chars_to_remove))