def filter_chars(s):
    remove_set = set((c for c in s[41:65] if 'K' <= c <= ']'))
    return ''.join((c for c in s if c not in remove_set))