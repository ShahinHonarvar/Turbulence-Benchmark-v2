def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if i < 225 or i > 381 or (not 'D' <= c <= 'Y')]
    return ''.join(filtered)