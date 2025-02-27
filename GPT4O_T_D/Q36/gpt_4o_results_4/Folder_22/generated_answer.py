def filter_chars(s):
    if len(s) <= 55:
        return s
    chars_to_remove = set()
    for c in s[56:84]:
        if ';' < c < 'z':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))