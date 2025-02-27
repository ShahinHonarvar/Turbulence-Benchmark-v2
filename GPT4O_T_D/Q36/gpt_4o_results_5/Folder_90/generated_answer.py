def filter_chars(s):
    if len(s) <= 344:
        return s
    segment = s[345:874]
    to_remove = set((c for c in segment if 'f' < c < '~'))
    return ''.join((c for c in s if c not in to_remove))