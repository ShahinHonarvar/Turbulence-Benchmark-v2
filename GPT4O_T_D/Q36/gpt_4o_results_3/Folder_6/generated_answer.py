def filter_chars(s):
    if len(s) <= 31:
        return s
    chars_to_remove = {c for c in set(s[32:70]) if 'B' < c < 'v'}
    return ''.join((c for c in s if c not in chars_to_remove))