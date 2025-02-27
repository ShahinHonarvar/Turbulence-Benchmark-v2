def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 25 <= i <= 97 and 'm' <= c <= 'w'))
    return ''.join((c for c in s if c not in to_remove))