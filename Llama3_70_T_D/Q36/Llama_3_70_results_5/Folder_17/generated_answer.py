def filter_chars(s):
    chars = [c for i, c in enumerate(s) if not (18 < i < 95 and 'K' < c < 'a')]
    return ''.join(chars)