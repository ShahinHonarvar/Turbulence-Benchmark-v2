def filter_chars(s):
    to_remove = [c for c in s[344:874] if 'f' < c < '~']
    for c in to_remove:
        s = s.replace(c, '')
    return s