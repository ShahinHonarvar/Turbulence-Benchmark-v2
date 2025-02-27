def filter_chars(s):
    to_remove = set()
    for c in s[422:854]:
        if 'D' < c < 'J':
            to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))