def filter_chars(s):
    chars = [c for c in s if not (63 <= s.index(c) <= 84 and 'E' <= c <= '~')]
    return ''.join(chars)