def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s[35:90]) if 'E' <= c <= 't'))
    return ''.join((c for c in s if c not in chars_to_remove))