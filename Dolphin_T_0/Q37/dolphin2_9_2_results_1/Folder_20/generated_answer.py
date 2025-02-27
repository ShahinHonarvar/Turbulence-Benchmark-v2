def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 25 or i > 97 or c < 'm' or (c > 'w')])