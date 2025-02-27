def filter_chars(s):
    chars = [c for c in s if not (29 <= s.index(c) <= 79 and 'K' <= c <= 'z')]
    return ''.join(chars)