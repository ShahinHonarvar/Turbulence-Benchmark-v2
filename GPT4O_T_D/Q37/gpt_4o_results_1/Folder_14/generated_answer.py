def filter_chars(s):
    if len(s) < 35:
        return s
    chars_to_remove = set((c for c in s[35:99] if 'A' <= c <= 'b'))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result