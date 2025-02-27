def filter_chars(s):
    if len(s) <= 714:
        return s
    chars_to_remove = {c for c in set(s[332:713]) if 'M' < c < '_'}
    return ''.join((c for c in s if c not in chars_to_remove))