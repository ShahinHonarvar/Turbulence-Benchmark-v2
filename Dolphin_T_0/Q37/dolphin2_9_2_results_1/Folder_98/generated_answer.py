def filter_chars(s):
    t = [c for c in s if c < 'R' or c > 't' or (c >= 'R' and c <= 't' and (s.index(c) < 8 or s.index(c) > 9))]
    return ''.join(t)