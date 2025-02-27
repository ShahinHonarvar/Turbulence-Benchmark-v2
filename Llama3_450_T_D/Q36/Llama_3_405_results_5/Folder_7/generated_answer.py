def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 502 < i < 946 and 'W' < c < 'y'))
    return ''.join((c for c in s if c not in chars_to_remove))