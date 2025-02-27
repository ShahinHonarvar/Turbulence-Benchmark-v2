def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 521 or i > 722 or c < '> ' or (c > '_')])