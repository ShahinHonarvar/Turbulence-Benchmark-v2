def filter_chars(s):
    to_remove = set()
    if len(s) > 591:
        for c in s[310:591]:
            if 'S' < c < 'm':
                to_remove.add(c)
    elif len(s) > 310:
        for c in s[310:-1]:
            if 'S' < c < 'm':
                to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))