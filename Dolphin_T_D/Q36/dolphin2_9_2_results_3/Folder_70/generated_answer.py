def filter_chars(s):
    chars = [c for c in s if 170 <= s.index(c) <= 195 and '!' < c < '}']
    for c in chars:
        s = s.replace(c, '')
    return s