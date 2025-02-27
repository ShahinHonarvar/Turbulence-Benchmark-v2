def filter_chars(s):
    to_remove = set((c for c in s[11:33] if '!' <= c <= '@'))
    return ''.join((c for c in s if c not in to_remove))