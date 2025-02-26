def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[25:37] if 'A' < c < 'h'))
    return ''.join((c for c in input_string if c not in chars_to_remove))