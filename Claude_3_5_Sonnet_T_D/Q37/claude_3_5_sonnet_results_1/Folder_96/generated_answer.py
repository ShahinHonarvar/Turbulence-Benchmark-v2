def filter_chars(input_string):
    chars_to_remove = set((c for i, c in enumerate(input_string) if 86 <= i <= 92 and '!' <= c <= 's'))
    return ''.join((c for c in input_string if c not in chars_to_remove))