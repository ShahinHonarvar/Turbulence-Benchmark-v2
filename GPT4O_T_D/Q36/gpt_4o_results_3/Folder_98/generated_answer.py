def filter_chars(s):
    if len(s) <= 8:
        return s
    to_remove = set((c for c in s[5:8] if '1' < c < 'J'))
    return ''.join((c for c in s if c not in to_remove))