def filter_chars(s):
    if len(s) <= 36:
        return s
    to_remove = set((c for c in s[36:60] if '!' < c < 'B'))
    return ''.join((c for c in s if c not in to_remove))