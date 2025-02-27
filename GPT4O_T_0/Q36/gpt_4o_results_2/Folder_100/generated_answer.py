def filter_chars(s):
    if len(s) <= 44:
        return s
    chars_to_remove = set((c for c in s[44:69] if 'B' < c < 'r'))
    return ''.join((c for c in s if c not in chars_to_remove))