def filter_chars(s):
    chars = [c for c in s if '8' <= c <= 'e' and 75 <= s.index(c) <= 99]
    return ''.join([c for c in s if c not in chars])