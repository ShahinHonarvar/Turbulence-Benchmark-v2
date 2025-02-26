def filter_chars(input_string):
    chars_to_remove = set((c for i, c in enumerate(input_string) if 54 <= i <= 83 and 'j' <= c <= 'v'))
    return ''.join((c for c in input_string if c not in chars_to_remove))