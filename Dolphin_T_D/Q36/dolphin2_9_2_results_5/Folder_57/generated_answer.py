def filter_chars(s):
    filtered = [c for c in s if 70 <= s.index(c) < 74 and (not 'A' < c < 'U')]
    return ''.join(filtered)