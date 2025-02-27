def filter_chars(s):
    remove_chars = set((c for c in s[38:100] if 'A' <= c <= 'Q'))
    return ''.join((c for c in s if c not in remove_chars))