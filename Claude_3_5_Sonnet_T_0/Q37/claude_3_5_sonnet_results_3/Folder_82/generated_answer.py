def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 12 <= i <= 25 and 'P' <= c <= 'x'))
    return ''.join((c for c in s if c not in chars_to_remove))