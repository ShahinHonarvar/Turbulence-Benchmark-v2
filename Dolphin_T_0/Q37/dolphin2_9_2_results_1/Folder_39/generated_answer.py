def filter_chars(s):
    chars = [c for c in s if 52 <= s.index(c) <= 81 and 'A' <= c <= 'U']
    return ''.join([c for c in s if c not in chars])