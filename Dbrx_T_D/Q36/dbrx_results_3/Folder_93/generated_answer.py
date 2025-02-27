def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 52 or i >= 88 or (c > '&' and c < 'c')))