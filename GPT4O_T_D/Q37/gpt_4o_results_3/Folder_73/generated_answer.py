def filter_chars(s):
    if len(s) <= 85:
        return s
    to_remove = set((c for c in s[22:86] if '7' <= c <= 'e'))
    return ''.join((c for c in s if c not in to_remove))