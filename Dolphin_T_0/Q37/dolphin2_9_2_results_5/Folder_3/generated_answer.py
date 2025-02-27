def filter_chars(s):
    chars_to_remove = [c for c in s[37:57] if '6' <= c <= '_']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s