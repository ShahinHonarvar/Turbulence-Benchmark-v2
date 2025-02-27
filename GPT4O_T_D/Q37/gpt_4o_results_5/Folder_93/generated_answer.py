def filter_chars(input_string):
    filter_range = input_string[38:70]
    chars_to_remove = set((c for c in filter_range if 'H' <= c <= 'e'))
    return ''.join((c for c in input_string if c not in chars_to_remove))