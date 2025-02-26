def filter_chars(s):
    to_remove = set((c for c in s[19:31] if 'H' < c < '|'))
    return ''.join((c for c in s if c not in to_remove))