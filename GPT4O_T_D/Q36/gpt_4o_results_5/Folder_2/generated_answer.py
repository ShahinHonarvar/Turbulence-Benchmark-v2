def filter_chars(s):
    indices_to_check = s[422:854]
    chars_to_remove = {c for c in indices_to_check if 'D' < c < 'J'}
    return ''.join((c for c in s if c not in chars_to_remove))