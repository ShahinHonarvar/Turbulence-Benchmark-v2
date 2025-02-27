def filter_chars(s):
    to_remove = set((c for c in s[24:80] if 'a' <= c <= 'f'))
    return ''.join((c for c in s if c not in to_remove))