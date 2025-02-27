def filter_chars(s):
    to_remove = [c for c in s[61:88] if '%' < c < 'q']
    for c in to_remove:
        s = s.replace(c, '')
    return s