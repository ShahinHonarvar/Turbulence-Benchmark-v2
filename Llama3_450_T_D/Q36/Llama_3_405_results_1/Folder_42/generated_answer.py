def filter_chars(s):
    chars_to_filter = set([c for i, c in enumerate(s) if 42 < i < 68 and 't' < c < 'x'])
    return ''.join((c for c in s if c not in chars_to_filter))