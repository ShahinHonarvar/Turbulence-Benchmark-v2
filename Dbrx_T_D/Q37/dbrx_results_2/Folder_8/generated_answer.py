def filter_chars(s):
    filtered_chars = [c for c in s if 41 <= s.index(c) <= 86 and 'S' <= c <= 's' or s.index(c) < 41 or s.index(c) > 86]
    return ''.join(filtered_chars)