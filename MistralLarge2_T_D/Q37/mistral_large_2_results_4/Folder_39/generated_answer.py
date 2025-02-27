def filter_chars(s):
    to_remove = set((c for c in s[52:82] if 'A' <= c <= 'U'))
    return ''.join((c for c in s if c not in to_remove))