def filter_chars(s):
    return ''.join((c for c in s if c < 'k' and c > '?' and (s.index(c) not in range(3, 8))))