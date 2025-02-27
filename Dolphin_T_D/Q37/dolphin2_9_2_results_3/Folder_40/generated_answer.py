def filter_chars(s):
    chars_to_filter = [c for c in s if 0 <= s.index(c) <= 1 and '*' <= c <= 's']
    return ''.join([c for c in s if c not in chars_to_filter])