def filter_chars(string):
    chars_to_remove = [c for c in string[30:33] if '%' < c < 'a']
    return ''.join((c for c in string if c not in chars_to_remove))