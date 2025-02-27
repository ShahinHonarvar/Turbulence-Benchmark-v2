def filter_chars(s):
    if len(s) > 93:
        chars_to_remove = {s[i] for i in range(87, 93) if 'E' < s[i] < '~'}
        s = ''.join((c for c in s if c not in chars_to_remove))
    return s