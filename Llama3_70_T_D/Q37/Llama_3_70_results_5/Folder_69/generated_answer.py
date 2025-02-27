def filter_chars(s):
    ascii_set = set([chr(i) for i in range(33, 121)])
    bad_chars = set((c for c in s if c in ascii_set))
    return ''.join((c for c in s if c not in bad_chars))