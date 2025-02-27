def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (61 < i < 88 and '%' < c < 'q')]
    return ''.join(filtered_chars)