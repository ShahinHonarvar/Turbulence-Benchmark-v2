def filter_chars(s):
    remove_chars = set((c for c in s[770:971] if '-' <= c <= 'D'))
    return ''.join((c for c in s if c not in remove_chars))