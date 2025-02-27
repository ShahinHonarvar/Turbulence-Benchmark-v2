def filter_chars(s):
    if len(s) <= 23:
        return s
    chars_to_remove = set()
    for c in s[24:83]:
        if 'f' < c < 'o':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))