def filter_chars(s):
    chars_to_remove = set((c for c in s[58:82] if 'F' < c < 'O'))
    return ''.join((c for c in s if c not in chars_to_remove))