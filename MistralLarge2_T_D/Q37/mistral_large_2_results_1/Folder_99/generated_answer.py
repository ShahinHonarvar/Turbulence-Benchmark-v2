def filter_chars(s):
    to_remove = set((c for c in s[373:902] if 'T' <= c <= 'h'))
    return ''.join((c for c in s if c not in to_remove))