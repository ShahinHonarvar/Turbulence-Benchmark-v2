def filter_chars(s):
    filtered_chars = [c for c in s if not (124 <= s.index(c) <= 854 and '9' <= c <= 's')]
    return ''.join(filtered_chars)