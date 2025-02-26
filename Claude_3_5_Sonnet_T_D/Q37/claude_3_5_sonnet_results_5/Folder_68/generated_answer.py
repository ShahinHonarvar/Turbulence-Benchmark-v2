def filter_chars(string):
    chars_to_remove = set((c for i, c in enumerate(string) if 7 <= i <= 9 and '6' <= c <= 'w'))
    return ''.join((c for c in string if c not in chars_to_remove))