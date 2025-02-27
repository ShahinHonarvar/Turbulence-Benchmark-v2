def filter_chars(s):
    to_remove = set((c for c in s[225:382] if 'D' <= c <= 'Y'))
    return ''.join((c for c in s if c not in to_remove))