def filter_chars(s):
    chars = [c for c in s if 63 <= s.index(c) <= 84 and 'E' <= c <= '~']
    return ''.join([c for c in s if c not in chars])