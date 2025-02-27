def filter_chars(s):
    if len(s) <= 344:
        return s
    to_remove = set()
    for c in s[345:874]:
        if 'f' < c < '~':
            to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))