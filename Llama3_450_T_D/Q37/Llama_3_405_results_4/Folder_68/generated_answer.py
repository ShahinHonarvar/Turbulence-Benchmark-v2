def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 7 <= i <= 9 and '6' <= c <= 'w'))
    return ''.join((c for c in s if c not in chars_to_remove))