def filter_chars(s):
    if len(s) < 90:
        return s
    chars_to_remove = set((c for c in s[64:89] if '*' < c < 'w'))
    return ''.join((c for c in s if c not in chars_to_remove))