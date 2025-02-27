def filter_chars(s):
    chars_to_filter = set([c for i, c in enumerate(s) if 124 <= i <= 854 and '9' <= c <= 's'])
    return ''.join([c for c in s if c not in chars_to_filter])