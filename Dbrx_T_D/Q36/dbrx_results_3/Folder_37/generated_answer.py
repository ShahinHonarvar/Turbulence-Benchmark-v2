def filter_chars(s):
    return ''.join((c for c in s if s.index(c) < 44 or s.index(c) >= 59 or '/' < c < '6'))