def filter_chars(string):
    chars_to_remove = set(range(ord('$') + 1, ord('?')))
    return ''.join((c for c in string if c not in chars_to_remove))