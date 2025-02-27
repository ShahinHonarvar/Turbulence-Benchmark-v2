def filter_chars(s):
    chars_to_remove = set((c for c in s[27:75] if 'A' < c < 'i'))
    return ''.join((c for c in s if c not in chars_to_remove))