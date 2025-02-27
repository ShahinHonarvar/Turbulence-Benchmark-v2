def filter_chars(s):
    if len(s) <= 5:
        return s
    chars_to_remove = set((c for c in s[1:6] if '$' <= c <= ';'))
    return ''.join((c for c in s if c not in chars_to_remove))