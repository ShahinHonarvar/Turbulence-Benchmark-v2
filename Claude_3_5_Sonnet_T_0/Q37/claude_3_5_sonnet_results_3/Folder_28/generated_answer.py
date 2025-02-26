def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 20 <= i <= 79 and '!' <= c <= 'T'))
    return ''.join((c for c in s if c not in chars_to_remove))