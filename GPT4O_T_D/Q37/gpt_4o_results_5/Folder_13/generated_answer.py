def filter_chars(s):
    to_remove = set((c for c in s[124:855] if '9' <= c <= 's'))
    return ''.join((c for c in s if c not in to_remove))