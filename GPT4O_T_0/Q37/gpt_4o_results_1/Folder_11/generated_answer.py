def filter_chars(s):
    if len(s) <= 29:
        return s
    chars_to_remove = set((c for c in s[29:98] if '-' <= c <= 'n'))
    return ''.join((c for c in s if c not in chars_to_remove))