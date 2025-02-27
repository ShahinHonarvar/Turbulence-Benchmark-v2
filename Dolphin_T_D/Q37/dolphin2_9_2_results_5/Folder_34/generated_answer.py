def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (54 <= i <= 62 and ')' <= c <= '9')])