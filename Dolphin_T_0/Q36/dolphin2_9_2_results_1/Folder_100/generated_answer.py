def filter_chars(s):
    to_remove = [c for c in s[43:69] if 'B' < c < 'r']
    for c in to_remove:
        s = s.replace(c, '')
    return s