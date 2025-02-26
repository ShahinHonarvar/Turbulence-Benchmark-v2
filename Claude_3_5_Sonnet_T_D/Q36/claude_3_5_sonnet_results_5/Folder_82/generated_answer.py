def filter_chars(input_string):
    chars_to_remove = set((c for c in input_string[70:97] if 'V' < c < 'j'))
    return ''.join((c for c in input_string if c not in chars_to_remove))