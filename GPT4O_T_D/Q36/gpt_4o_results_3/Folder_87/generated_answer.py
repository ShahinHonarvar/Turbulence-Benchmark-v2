def filter_chars(s):
    return ''.join([c for idx, c in enumerate(s) if idx <= 32 or idx >= 61 or (not '3' < c < 'D')])