def filter_chars(s):
    chars_to_remove = set((c for c in s[476:948] if 'b' < c < 'd'))
    return ''.join((c for c in s if c not in chars_to_remove))