def filter_chars(string):
    chars_to_remove = set((c for c in string[55:92] if 'J' < c < 'X'))
    return ''.join((c for c in string if c not in chars_to_remove))