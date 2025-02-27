def filter_chars(s):
    chars_to_remove = set(s[51:78]).intersection({'V', 'W', 'X', 'Y'})
    return ''.join((c for c in s if c not in chars_to_remove))