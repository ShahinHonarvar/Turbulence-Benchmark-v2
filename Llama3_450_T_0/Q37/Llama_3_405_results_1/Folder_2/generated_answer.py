def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 477 <= i <= 984 and ',' <= c <= 'V'))
    return ''.join((c for c in s if c not in chars_to_remove))