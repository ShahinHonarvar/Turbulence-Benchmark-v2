def filter_chars(s):
    chars_to_remove = set((c for c in s[8:10] if 'R' <= c <= 't'))
    return ''.join((c for c in s if c not in chars_to_remove))