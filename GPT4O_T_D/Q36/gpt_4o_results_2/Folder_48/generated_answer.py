def filter_chars(s):
    if len(s) <= 154:
        return s
    to_remove = set((c for c in s[155:222] if 'A' < c < 'f'))
    return ''.join((c for c in s if c not in to_remove))