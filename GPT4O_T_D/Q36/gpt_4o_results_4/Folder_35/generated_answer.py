def filter_chars(string):
    if len(string) <= 658:
        return string
    chars_to_remove = set((c for c in string[164:658] if '(' < c < ']'))
    return ''.join((c for c in string if c not in chars_to_remove))