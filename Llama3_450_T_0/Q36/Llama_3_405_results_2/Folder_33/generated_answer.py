def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 299 < i < 418 and '9' < c < 'P'))
    return ''.join((c for c in s if c not in chars_to_remove))