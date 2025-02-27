def filter_chars(s):
    to_remove = set((c for c in s[1:9] if '8' < c < 'm'))
    return ''.join((c for c in s if c not in to_remove))