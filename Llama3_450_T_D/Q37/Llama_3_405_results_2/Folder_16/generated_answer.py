def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 225 <= i <= 381 and 'D' <= c <= 'Y'))
    return ''.join((c for c in s if c not in chars_to_remove))