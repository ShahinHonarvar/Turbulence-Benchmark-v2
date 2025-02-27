def filter_chars(s):
    chars_to_remove = {c for c in s[503:946] if 'W' < c < 'y'}
    return ''.join((c for c in s if c not in chars_to_remove))