def filter_chars(s):
    indices_to_check = range(32, 47)
    chars_to_remove = set((c for i, c in enumerate(s) if i in indices_to_check and '0' <= c <= 'k'))
    return ''.join((c for c in s if c not in chars_to_remove))