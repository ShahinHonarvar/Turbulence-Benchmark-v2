def filter_chars(s):
    to_remove = [c for c in s[43:83] if ':' < c < 'Q']
    for c in to_remove:
        s = s.replace(c, '')
    return s