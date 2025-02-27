def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[23:90]) if 'w' <= c <= '{']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s