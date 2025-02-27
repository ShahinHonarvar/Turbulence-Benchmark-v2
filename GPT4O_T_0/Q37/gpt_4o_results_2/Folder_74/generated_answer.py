def filter_chars(s):
    if len(s) <= 32:
        return s
    chars_to_remove = set((c for c in s[19:33] if 'f' <= c <= 'o'))
    return ''.join((c for c in s if c not in chars_to_remove))