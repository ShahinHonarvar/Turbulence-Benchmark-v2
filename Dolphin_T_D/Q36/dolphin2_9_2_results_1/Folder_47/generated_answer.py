def filter_chars(s):
    chars = [c for c in s if 'F' < c < 'n' and 45 <= s.index(c) < 57]
    for c in chars:
        s = s.replace(c, '')
    return s