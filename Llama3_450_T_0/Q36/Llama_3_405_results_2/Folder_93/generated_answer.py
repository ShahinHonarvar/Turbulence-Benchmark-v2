def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 52 < i < 88 and '&' < c < 'c'))
    return ''.join((c for c in s if c not in chars_to_remove))