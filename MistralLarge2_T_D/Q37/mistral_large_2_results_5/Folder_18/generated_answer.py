def filter_chars(s):
    to_remove = set((c for c in s[770:971] if '-' <= c <= 'D'))
    return ''.join((c for c in s if c not in to_remove))