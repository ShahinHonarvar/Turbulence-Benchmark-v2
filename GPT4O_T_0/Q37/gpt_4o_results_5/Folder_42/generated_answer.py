def filter_chars(s):
    if len(s) < 75:
        return s
    chars_to_remove = set((c for c in s[73:75] if 'U' <= c <= 'l'))
    return ''.join((c for c in s if c not in chars_to_remove))