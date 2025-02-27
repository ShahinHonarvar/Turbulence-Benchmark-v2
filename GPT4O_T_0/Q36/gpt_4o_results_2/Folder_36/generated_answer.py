def filter_chars(s):
    if len(s) <= 484:
        return s
    chars_to_remove = set((c for c in s[284:484] if 'l' < c < 't'))
    return ''.join((c for c in s if c not in chars_to_remove))