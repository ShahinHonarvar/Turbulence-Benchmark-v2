def filter_chars(s):
    if len(s) <= 71:
        return s
    chars_to_remove = set((c for c in s[71:95] if 'K' <= c <= 'a'))
    return ''.join((c for c in s if c not in chars_to_remove))