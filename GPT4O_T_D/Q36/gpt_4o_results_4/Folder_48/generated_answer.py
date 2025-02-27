def filter_chars(s):
    remove_chars = {c for c in s[155:222] if 'A' < c < 'f'}
    return ''.join((c for c in s if c not in remove_chars))