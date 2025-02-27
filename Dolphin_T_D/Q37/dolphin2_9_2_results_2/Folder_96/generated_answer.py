def filter_chars(s):
    chars = [c for c in s if 86 <= s.index(c) <= 92 and '!' <= c <= 's']
    for c in chars:
        s = s.replace(c, '')
    return s