def filter_chars(s):
    chars = [c for c in s if not (ord('3') < ord(c) < ord('B') and s.index(c) > 18 and (s.index(c) < 64))]
    return ''.join([c for c in s if c not in chars])