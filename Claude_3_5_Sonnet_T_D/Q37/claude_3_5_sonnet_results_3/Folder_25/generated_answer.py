def filter_chars(string):
    chars_to_remove = set((c for i, c in enumerate(string) if 31 <= i <= 38 and ';' <= c <= 'g'))
    return ''.join((c for c in string if c not in chars_to_remove))