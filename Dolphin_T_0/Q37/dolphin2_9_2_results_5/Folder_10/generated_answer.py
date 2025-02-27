def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 63 or i > 84 or (c < 'E' or c > '~')])