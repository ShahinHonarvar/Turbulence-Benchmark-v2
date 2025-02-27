def filter_chars(s):
    if len(s) < 515:
        return s
    to_remove = set((c for c in s[515:539] if '+' <= c <= '}'))
    return ''.join((c for c in s if c not in to_remove))