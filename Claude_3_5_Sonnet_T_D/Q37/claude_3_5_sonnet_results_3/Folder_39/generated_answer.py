def filter_chars(string):
    chars_to_remove = set((c for i, c in enumerate(string) if 52 <= i <= 81 and 'A' <= c <= 'U'))
    return ''.join((c for c in string if c not in chars_to_remove))