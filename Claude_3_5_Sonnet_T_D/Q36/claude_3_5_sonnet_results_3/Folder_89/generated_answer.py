def filter_chars(string):
    chars_to_remove = set((c for c in string[58:69] if '(' < c < 'W'))
    return ''.join((c for c in string if c not in chars_to_remove))