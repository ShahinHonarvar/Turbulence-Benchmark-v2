def filter_chars(input_string):
    chars_to_remove = set((c for i, c in enumerate(input_string) if 225 <= i <= 381 and 'D' <= c <= 'Y'))
    return ''.join((c for c in input_string if c not in chars_to_remove))