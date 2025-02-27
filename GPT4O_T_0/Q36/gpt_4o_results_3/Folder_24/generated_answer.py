def filter_chars(s):
    if len(s) <= 11:
        return s
    chars_to_remove = set((c for c in s[11:15] if 't' < c < 'v'))
    return ''.join((c for c in s if c not in chars_to_remove))