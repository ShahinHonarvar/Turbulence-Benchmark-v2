def filter_chars(s):
    if len(s) <= 2:
        return s
    to_remove = set((c for c in s[2:6] if ',' < c < 'f'))
    return ''.join((c for c in s if c not in to_remove))