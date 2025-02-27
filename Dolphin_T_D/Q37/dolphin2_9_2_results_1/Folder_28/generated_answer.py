def filter_chars(s):
    chars = [c for c in s if 20 <= s.index(c) <= 79 and '!' <= c <= 'T']
    for c in chars:
        s = s.replace(c, '')
    return s