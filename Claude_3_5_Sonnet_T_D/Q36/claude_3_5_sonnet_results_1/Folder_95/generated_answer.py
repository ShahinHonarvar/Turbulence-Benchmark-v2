def filter_chars(string):
    chars_to_remove = set((c for c in string[56:86] if '+' < c < 'w'))
    return ''.join((c for c in string if c not in chars_to_remove))