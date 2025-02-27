def filter_chars(s):
    chars = [c for c in s if 71 <= s.index(c) <= 94 and 'K' <= c <= 'a']
    for c in chars:
        s = s.replace(c, '')
    return s