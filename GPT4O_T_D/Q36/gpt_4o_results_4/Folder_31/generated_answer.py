def filter_chars(s):
    to_remove = set((c for c in set(s[15:75]) if '9' < c < 'K'))
    return ''.join((c for c in s if c not in to_remove))