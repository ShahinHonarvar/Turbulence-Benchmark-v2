def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 86 < i < 93 and 'E' < c < '~']
    return ''.join((c for c in s if c not in chars_to_remove))