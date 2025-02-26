def filter_chars(input_string):
    chars_to_remove = set((c for i, c in enumerate(input_string) if 7 <= i <= 8 and 'B' <= c <= 'H'))
    return ''.join((c for c in input_string if c not in chars_to_remove))