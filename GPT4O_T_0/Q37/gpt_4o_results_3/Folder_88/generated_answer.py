def filter_chars(s):
    if len(s) <= 80:
        return s
    chars_to_remove = set((c for c in s[69:81] if '@' <= c <= 'p'))
    return ''.join((c for c in s if c not in chars_to_remove))