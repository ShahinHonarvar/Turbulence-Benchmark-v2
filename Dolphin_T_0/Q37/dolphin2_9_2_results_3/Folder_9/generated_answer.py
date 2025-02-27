def filter_chars(s):
    return ''.join([c for c in s if (c < 'A' or c > 'Q') or (0 <= s.index(c) < 38 or 100 <= s.index(c))])