def filter_chars(s):
    if len(s) <= 3:
        return s
    chars_to_remove = set((c for c in s[3:7] if 'h' < c < 'k'))
    return ''.join((c for c in s if c not in chars_to_remove))