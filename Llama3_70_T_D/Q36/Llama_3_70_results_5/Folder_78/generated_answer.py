def filter_chars(s):
    chars_to_remove = [c for c in s[29:33] if '%' < c < 'a']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s