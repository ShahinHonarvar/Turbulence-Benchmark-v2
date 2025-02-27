def filter_chars(s):
    if len(s) < 23:
        return s
    chars_to_remove = set((c for c in s[19:23] if ']' <= c <= 't'))
    return ''.join((c for c in s if c not in chars_to_remove))