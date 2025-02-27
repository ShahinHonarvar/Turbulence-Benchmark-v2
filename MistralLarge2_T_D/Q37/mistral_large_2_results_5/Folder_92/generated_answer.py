def filter_chars(s):
    to_remove = set((c for c in s[4:5] if '7' <= c <= 'o'))
    return ''.join((c for c in s if c not in to_remove))