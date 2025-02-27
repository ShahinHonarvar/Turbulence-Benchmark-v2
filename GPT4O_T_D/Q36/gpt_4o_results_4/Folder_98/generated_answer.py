def filter_chars(s):
    chars_to_remove = set((c for c in s[5:8] if '1' < c < 'J'))
    return ''.join((c for c in s if c not in chars_to_remove))