def filter_chars(s):
    if len(s) <= 45:
        return s
    to_remove = set((c for c in s[24:45] if '3' < c < 'I'))
    return ''.join((c for c in s if c not in to_remove))