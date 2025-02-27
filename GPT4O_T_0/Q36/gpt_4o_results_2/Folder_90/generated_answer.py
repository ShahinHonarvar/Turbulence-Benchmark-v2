def filter_chars(s):
    if len(s) <= 344:
        return s
    start = 345
    end = min(874, len(s) - 1)
    chars_to_remove = set((c for c in s[start:end] if 'f' < c < '~'))
    return ''.join((c for c in s if c not in chars_to_remove))