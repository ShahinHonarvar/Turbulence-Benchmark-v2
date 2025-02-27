def filter_chars(s):
    to_remove = set((c for c in s[722:833] if 'K' <= c <= 'm'))
    return ''.join((c for c in s if c not in to_remove))