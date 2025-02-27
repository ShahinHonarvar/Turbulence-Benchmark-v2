def filter_chars(s):
    chars_to_remove = [c for c in s if 33 <= ord(c) <= 70 and '7' <= c <= 'k']
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s