def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (41 <= i <= 64 and 'K' <= c <= ']')]
    return ''.join(filtered_chars)