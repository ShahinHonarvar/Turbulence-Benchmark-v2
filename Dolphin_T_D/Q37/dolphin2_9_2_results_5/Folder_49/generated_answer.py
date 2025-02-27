def filter_chars(s):
    chars = [c for c in s if '*' <= c <= 'b' and 42 <= s.index(c) <= 97]
    for c in chars:
        s = s.replace(c, '')
    return s