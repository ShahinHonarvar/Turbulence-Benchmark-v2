def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (i >= 69 and i < 87 and (c > '#') and (c < 'L'))))