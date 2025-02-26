def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[309:591] if 'S' < c < 'm'))
    return ''.join((c for c in input_string if c not in chars_to_remove))