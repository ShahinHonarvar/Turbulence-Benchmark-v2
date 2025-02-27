def filter_chars(s):
    filtered_chars = [c for c in s if not (15 <= s.index(c) <= 55 and 'W' <= c <= '{')]
    return ''.join(filtered_chars)