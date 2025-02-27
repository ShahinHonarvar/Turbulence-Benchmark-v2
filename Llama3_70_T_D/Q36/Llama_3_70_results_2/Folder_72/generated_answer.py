def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (44 < i < 68 and 'W' < c < 'x')]
    return ''.join(filtered_chars)