def filter_chars(s):
    chars_to_remove = set((c for c in s[21:25] if '5' < c < '}'))
    return ''.join((c for c in s if c not in chars_to_remove))