def filter_chars(s):
    chars_to_remove = set((c for c in s[57:86] if '+' < c < 'w'))
    return ''.join((c for c in s if c not in chars_to_remove))