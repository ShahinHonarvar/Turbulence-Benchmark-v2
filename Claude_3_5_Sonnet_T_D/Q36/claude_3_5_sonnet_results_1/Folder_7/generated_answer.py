def filter_chars(string):
    chars_to_remove = set((c for c in string[502:946] if 'W' < c < 'y'))
    return ''.join((c for c in string if c not in chars_to_remove))