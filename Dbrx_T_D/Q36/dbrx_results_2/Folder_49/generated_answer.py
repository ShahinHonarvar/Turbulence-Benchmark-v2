def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i >= 46 and i < 91 and (c > 'B') and (c < 'G')))