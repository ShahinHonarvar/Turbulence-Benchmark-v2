def filter_chars(s):
    chars_to_remove = set(s[8:10]).intersection(range(ord('R'), ord('t') + 1))
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s