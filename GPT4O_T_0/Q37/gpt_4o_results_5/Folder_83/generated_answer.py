def filter_chars(s):
    if len(s) < 30:
        return s
    chars_to_remove = set((c for c in s[29:80] if 'K' <= c <= 'z'))
    return ''.join((c for c in s if c not in chars_to_remove))