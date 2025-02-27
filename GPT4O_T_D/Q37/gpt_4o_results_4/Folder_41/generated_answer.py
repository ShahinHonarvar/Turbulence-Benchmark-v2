def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s[26:65]) if 'V' <= c <= 'o'))
    return ''.join((c for c in s if c not in to_remove))