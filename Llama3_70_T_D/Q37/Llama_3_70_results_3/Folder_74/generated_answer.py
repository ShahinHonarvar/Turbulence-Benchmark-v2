def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s[19:33], 19) if 'f' <= c <= 'o'))
    return ''.join((c for c in s if c not in chars_to_remove))