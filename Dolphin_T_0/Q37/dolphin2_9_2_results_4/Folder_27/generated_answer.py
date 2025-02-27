def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (43 <= i <= 80 and '=' <= c <= 'E')])