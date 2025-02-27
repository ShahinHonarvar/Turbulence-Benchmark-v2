def filter_chars(s):
    chars_to_remove = {c for c in s[670:888] if 'B' < c < 'Y'}
    return ''.join((c for c in s if c not in chars_to_remove))