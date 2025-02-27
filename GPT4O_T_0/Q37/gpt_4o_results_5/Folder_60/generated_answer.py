def filter_chars(s):
    to_remove = set((c for c in s[12:78] if ':' <= c <= 'L'))
    return ''.join((c for c in s if c not in to_remove))