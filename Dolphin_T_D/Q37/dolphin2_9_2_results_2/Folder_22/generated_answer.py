def filter_chars(s):
    filtered = [c for c in s if 33 <= s.index(c) <= 70 and '7' <= c <= 'k' or (s.index(c) < 33 or s.index(c) > 70)]
    return ''.join(filtered)