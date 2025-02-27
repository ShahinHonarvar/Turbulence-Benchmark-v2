def filter_chars(s):
    if len(s) < 31:
        return s
    chars_to_remove = set((c for c in s[31:39] if ';' <= c <= 'g'))
    return ''.join((c for c in s if c not in chars_to_remove))