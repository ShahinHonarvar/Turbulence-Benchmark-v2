def filter_chars(s):
    chars_to_remove = set((c for c in s[46:68] if 'H' < c < 's'))
    return ''.join((c for c in s if c not in chars_to_remove))