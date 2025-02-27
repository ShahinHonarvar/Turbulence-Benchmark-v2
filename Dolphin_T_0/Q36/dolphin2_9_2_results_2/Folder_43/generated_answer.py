def filter_chars(s):
    chars = [c for c in s if c > 'A' and c < 'i' and (27 <= s.index(c) < 75)]
    for c in chars:
        s = s.replace(c, '')
    return s