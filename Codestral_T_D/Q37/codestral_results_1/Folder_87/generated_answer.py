def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (18 <= i <= 81 and 'W' <= c <= '[')])