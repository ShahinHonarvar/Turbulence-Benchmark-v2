def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 379 or i > 898 or (not 'M' <= c <= 'v')))