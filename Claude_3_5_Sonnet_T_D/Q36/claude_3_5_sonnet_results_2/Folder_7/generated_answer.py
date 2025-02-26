def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[502:946] if 'W' < c < 'y'))
    return ''.join((c for c in input_string if c not in chars_to_remove))