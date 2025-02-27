def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (48 < i < 75 and '6' < c < '_')])