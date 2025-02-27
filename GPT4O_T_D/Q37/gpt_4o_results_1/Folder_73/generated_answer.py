def filter_chars(s):
    filtered = [c for c in s if not (22 <= s.index(c) <= 85 and '7' <= c <= 'e')]
    return ''.join(filtered)