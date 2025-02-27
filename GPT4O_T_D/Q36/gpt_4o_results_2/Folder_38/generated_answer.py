def filter_chars(s):
    chars_to_remove = {c for c in s[45:48] if '+' < c < 'l'}
    return ''.join((c for c in s if c not in chars_to_remove))