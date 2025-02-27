def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[36:80] if '2' <= c <= 's'))
    return ''.join((c for c in input_string if c not in chars_to_remove))