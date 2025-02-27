def filter_chars(s):
    to_remove = set((c for c in s[51:92] if 'A' < c < 'Q'))
    return ''.join((c for c in s if c not in to_remove))