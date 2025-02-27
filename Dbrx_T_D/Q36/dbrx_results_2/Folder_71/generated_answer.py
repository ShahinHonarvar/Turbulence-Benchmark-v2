def filter_chars(s):
    return ''.join((c for c in s if s.index(c) < 82 or s.index(c) >= 89 or (c <= '*' or c >= '[') for c in s))