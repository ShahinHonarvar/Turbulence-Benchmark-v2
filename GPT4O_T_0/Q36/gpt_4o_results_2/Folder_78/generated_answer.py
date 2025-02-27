def filter_chars(s):
    if len(s) <= 30:
        return s
    chars_to_remove = set((c for c in s[30:33] if '%' < c < 'a'))
    return ''.join((c for c in s if c not in chars_to_remove))