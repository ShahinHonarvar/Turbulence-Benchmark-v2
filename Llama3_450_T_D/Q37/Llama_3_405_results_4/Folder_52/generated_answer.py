def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 54 <= i <= 83 and 'j' <= c <= 'v'))
    return ''.join((c for c in s if c not in chars_to_remove))