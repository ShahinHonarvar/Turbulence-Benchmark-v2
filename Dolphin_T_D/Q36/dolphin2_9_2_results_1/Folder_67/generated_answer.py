def filter_chars(s):
    chars_to_remove = [c for c in s[18:31] if 'H' < c < '|']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s