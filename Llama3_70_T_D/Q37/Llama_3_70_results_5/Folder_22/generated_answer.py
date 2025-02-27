def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (33 <= i <= 70 and '7' <= c <= 'k')]
    return ''.join(filtered_chars)