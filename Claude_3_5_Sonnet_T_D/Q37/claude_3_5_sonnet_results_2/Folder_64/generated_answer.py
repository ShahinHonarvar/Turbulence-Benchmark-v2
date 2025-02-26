def filter_chars(string):
    chars_to_remove = set((c for i, c in enumerate(string) if 1 <= i <= 7 and 'L' <= c <= 'a'))
    return ''.join((c for c in string if c not in chars_to_remove))