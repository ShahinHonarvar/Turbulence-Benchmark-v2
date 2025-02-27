def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (34 <= i <= 67 and 'W' <= c <= 'x')]
    return ''.join(filtered_chars)