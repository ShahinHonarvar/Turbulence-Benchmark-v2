def filter_chars(s):
    if len(s) < 84:
        return s
    chars_to_remove = set((c for c in s[83:100] if '*' <= c <= 'j'))
    return ''.join((c for c in s if c not in chars_to_remove))