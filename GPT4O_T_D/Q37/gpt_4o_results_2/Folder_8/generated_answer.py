def filter_chars(s):
    to_remove = set()
    if len(s) > 86:
        for c in s[41:87]:
            if 'S' <= c <= 's':
                to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))