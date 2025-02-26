def filter_chars(s):
    chars_to_remove = set((c for c in s[55:80] if 'S' < c < 's'))
    return ''.join((c for c in s if c not in chars_to_remove))