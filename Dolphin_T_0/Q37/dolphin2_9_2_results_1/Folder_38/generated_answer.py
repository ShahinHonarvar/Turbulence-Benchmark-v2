def filter_chars(s):
    to_remove = [c for c in s[24:80] if 'a' <= c <= 'f']
    for c in to_remove:
        s = s.replace(c, '')
    return s