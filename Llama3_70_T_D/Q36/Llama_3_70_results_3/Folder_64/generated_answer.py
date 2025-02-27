def filter_chars(s):
    del_chars = set((c for c in s[1:7] if '3' < c < '^'))
    return ''.join((c for c in s if c not in del_chars))