def filter_chars(s):
    return ''.join((c for c in s if 11 <= s.index(c) <= 72 and (not 'i' <= c <= 'v') or s.index(c) > 72 or s.index(c) < 11))