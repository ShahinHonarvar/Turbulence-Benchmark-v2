def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 88 <= i <= 90 and 'J' <= c <= 'Q'))
    return ''.join((c for c in s if c not in chars_to_remove))