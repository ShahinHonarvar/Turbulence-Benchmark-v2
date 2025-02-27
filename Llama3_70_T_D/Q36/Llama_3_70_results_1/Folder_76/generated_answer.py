def filter_chars(s):
    chars_to_remove = [c for c in s[669:888] if 'B' < c < 'Y']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s