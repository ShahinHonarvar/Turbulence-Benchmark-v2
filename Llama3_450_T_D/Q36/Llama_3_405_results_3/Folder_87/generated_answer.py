def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 32 < i < 61 and '3' < c < 'D'))
    return ''.join((c for c in s if c not in chars_to_remove))