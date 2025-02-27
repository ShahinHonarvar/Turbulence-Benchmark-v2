def filter_chars(s):
    to_remove = set((c for c in s[73:93] if '<' < c < 'J'))
    return ''.join((c for c in s if c not in to_remove))