def filter_chars(s):
    if len(s) < 91:
        return s
    chars_to_remove = set((c for c in s[88:91] if 'J' <= c <= 'Q'))
    return ''.join((c for c in s if c not in chars_to_remove))