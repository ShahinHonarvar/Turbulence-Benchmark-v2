def filter_chars(s):
    if len(s) < 38:
        return s
    chars_to_remove = set((c for c in s[38:100] if 'A' <= c <= 'Q'))
    return ''.join((c for c in s if c not in chars_to_remove))