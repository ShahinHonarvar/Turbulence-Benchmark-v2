def filter_chars(s):
    chars_to_remove = [c for c in s[27:75] if 'A' < c < 'i']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s