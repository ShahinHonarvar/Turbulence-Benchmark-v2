def filter_chars(s):
    to_remove = set((c for c in s[38:70] if 'H' <= c <= 'e'))
    return ''.join((c for c in s if c not in to_remove))