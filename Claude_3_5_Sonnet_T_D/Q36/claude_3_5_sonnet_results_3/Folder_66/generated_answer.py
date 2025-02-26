def filter_chars(string):
    chars_to_remove = set((c for c in string[39:87] if '!' < c < '}'))
    return ''.join((c for c in string if c not in chars_to_remove))