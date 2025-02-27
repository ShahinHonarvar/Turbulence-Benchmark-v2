def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 19 < i < 69 and '<' < c < 'C'))
    return ''.join((c for c in s if c not in chars_to_remove))