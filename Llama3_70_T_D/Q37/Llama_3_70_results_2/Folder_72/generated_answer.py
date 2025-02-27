def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[35:52]) if 'H' <= c <= 's']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s