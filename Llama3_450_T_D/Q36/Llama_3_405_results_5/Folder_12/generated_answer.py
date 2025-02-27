def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 32 < i < 84 and 'm' < c < 'w']
    return ''.join((c for c in s if c not in chars_to_remove))