def filter_chars(s):
    chars_to_remove = set((c for c in set(s[344:665]) if '%' < c < 'U'))
    return ''.join((c for c in s if c not in chars_to_remove))