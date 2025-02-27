def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 138 or i > 920 or (not '6' <= c <= 'A')))