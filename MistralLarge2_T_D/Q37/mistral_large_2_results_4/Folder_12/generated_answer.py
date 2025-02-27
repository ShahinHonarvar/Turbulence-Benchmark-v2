def filter_chars(s):
    to_remove = set((c for c in s[19:91] if 'F' <= c <= 'h'))
    return ''.join((c for c in s if c not in to_remove))