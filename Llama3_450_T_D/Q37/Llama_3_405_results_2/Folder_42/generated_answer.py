def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 73 <= i <= 74 and 'U' <= c <= 'l'))
    return ''.join((c for c in s if c not in chars_to_filter))