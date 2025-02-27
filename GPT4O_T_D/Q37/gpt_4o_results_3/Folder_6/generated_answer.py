def filter_chars(s):
    if len(s) < 14:
        return s
    chars_to_remove = set((c for c in s[13:29] if 'c' <= c <= 'n'))
    return ''.join((c for c in s if c not in chars_to_remove))