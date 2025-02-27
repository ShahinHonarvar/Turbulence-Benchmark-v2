def filter_chars(s):
    to_remove = set((c for c in s[309:591] if 'S' < c < 'm'))
    return ''.join((c for c in s if c not in to_remove))