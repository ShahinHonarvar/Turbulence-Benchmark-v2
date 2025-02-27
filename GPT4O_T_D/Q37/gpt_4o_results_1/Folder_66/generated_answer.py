def filter_chars(s):
    to_remove = set((c for c in set(s[27:86]) if 'c' <= c <= 'i'))
    return ''.join((c for c in s if c not in to_remove))