def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 1 <= i <= 7 and 'L' <= c <= 'a'))
    return ''.join((c for c in s if c not in chars_to_remove))