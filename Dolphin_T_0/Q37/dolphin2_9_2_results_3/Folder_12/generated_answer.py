def filter_chars(s):
    to_remove = [c for c in s[19:91] if 'F' <= c <= 'h']
    for c in to_remove:
        s = s.replace(c, '')
    return s