def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (32 < i < 61 and '3' < c < 'D')))