def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 7 <= i <= 8 and 'B' <= c <= 'H'))
    return ''.join((c for c in s if c not in chars_to_remove))