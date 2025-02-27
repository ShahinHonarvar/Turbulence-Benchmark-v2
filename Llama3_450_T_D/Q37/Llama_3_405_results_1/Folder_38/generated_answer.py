def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 24 <= i <= 79 and 'a' <= c <= 'f'))
    return ''.join((c for c in s if c not in chars_to_remove))