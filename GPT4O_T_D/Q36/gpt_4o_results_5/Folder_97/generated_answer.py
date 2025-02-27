def filter_chars(s):
    if len(s) <= 591:
        return s
    chars_to_remove = {c for c in s[310:591] if 'S' < c < 'm'}
    return ''.join((c for c in s if c not in chars_to_remove))