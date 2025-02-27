def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 55 < i < 66 and 'f' < c < '|'))
    return ''.join((c for c in s if c not in chars_to_filter))