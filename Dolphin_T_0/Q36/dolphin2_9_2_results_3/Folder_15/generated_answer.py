def filter_chars(s):
    filtered_chars = [c for c in s if not (2 <= s.index(c) < 7 and 'h' < c < 'k')]
    return ''.join(filtered_chars)