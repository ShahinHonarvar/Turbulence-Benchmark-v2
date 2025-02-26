def filter_chars(string):
    chars_to_remove = set((c for c in string[59:82] if 'F' < c < 'O'))
    return ''.join((c for c in string if c not in chars_to_remove))