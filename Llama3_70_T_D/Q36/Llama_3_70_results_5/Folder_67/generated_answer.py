def filter_chars(s):
    chars_to_remove = set(s[18:31])
    chars_to_remove = [c for c in chars_to_remove if 'H' < c < '|']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s