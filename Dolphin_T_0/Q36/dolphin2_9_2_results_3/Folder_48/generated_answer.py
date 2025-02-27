def filter_chars(s):
    to_remove = [c for i, c in enumerate(s) if 154 <= i < 222 and 'A' < c < 'f']
    for c in to_remove:
        s = s.replace(c, '')
    return s