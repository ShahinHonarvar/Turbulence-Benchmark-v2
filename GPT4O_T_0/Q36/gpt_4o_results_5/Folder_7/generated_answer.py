def filter_chars(s):
    if len(s) <= 502:
        return s
    chars_to_remove = set((c for c in s[503:946] if 'W' < c < 'y'))
    return ''.join((c for c in s if c not in chars_to_remove))