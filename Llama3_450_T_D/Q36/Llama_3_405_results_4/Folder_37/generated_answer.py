def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 44 < i < 59 and '/' < c < '6'))
    return ''.join((c for c in s if c not in chars_to_remove))