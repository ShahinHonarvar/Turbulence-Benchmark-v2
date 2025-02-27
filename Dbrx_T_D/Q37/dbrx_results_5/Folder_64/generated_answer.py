def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 1 or i > 7 or (c < 'L' or c > 'a')])