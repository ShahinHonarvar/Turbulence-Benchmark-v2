def filter_chars(s):
    remove_chars = set((c for c in s[52:88] if '&' < c < 'c'))
    return ''.join((c for c in s if c not in remove_chars))