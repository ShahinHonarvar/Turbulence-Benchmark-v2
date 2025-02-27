def filter_chars(s):
    to_remove = set((c for c in s[348:853] if 'J' <= c <= 'b'))
    return ''.join((c for c in s if c not in to_remove))