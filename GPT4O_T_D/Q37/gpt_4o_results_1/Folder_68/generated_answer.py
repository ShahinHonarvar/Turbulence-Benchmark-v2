def filter_chars(s):
    if len(s) < 8:
        return s
    to_remove = set((c for c in s[7:10] if '6' <= c <= 'w'))
    return ''.join((c for c in s if c not in to_remove))