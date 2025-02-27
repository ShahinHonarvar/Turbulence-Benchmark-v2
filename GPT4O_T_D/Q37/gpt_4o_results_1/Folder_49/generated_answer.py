def filter_chars(s):
    if len(s) <= 97:
        return s
    chars_to_remove = set((c for c in s[42:98] if '*' <= c <= 'b'))
    return ''.join((c for c in s if c not in chars_to_remove))