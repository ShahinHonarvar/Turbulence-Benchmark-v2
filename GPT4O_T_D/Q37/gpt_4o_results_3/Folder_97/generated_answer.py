def filter_chars(s):
    if len(s) < 236:
        return s
    chars_to_remove = set((c for c in s[227:236] if 'D' <= c <= 'u'))
    return ''.join((c for c in s if c not in chars_to_remove))