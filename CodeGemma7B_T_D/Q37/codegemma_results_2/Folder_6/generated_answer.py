def filter_chars(s):
    return ''.join([c for c in s if not (c >= 'c' and c <= 'n' and (13 <= s.index(c) <= 28))])