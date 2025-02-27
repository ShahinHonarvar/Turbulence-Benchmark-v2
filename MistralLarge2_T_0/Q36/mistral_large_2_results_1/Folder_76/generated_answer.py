def filter_chars(s):
    chars_to_remove = set((c for c in s[669:888] if 'B' < c < 'Y'))
    return ''.join((c for c in s if c not in chars_to_remove))