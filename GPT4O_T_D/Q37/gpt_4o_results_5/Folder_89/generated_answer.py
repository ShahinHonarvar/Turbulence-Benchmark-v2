def filter_chars(s):
    if len(s) < 12:
        return s
    filter_chars = set()
    for c in s[11:33]:
        if '!' <= c <= '@':
            filter_chars.add(c)
    return ''.join((c for c in s if c not in filter_chars))