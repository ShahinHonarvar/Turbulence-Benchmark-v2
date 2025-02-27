def filter_chars(s):
    new_chars = [c for c in s if not (114 <= s.index(c) <= 639 and '!' <= c <= 'x')]
    return ''.join(new_chars)