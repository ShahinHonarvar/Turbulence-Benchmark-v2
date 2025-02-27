def filter_chars(s):
    if len(s) <= 52:
        return s
    to_remove = set((c for c in s[52:82] if 'A' <= c <= 'U'))
    return ''.join((c for c in s if c not in to_remove))