def filter_chars(s):
    to_remove = set((c for c in s[4:9] if '*' < c < 'E'))
    return ''.join((c for c in s if c not in to_remove))