def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (225 <= i <= 381 and 'D' <= c <= 'Y')]
    return ''.join(filtered_chars)