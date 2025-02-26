def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[82:89] if 'f' < c < '{'))
    return ''.join((c for c in input_string if c not in chars_to_remove))