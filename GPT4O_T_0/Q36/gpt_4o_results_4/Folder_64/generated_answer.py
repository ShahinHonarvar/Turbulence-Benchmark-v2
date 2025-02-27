def filter_chars(s):
    if len(s) <= 2:
        return s
    chars_to_remove = {c for c in s[2:7] if '3' < c < '^'}
    return ''.join((c for c in s if c not in chars_to_remove))