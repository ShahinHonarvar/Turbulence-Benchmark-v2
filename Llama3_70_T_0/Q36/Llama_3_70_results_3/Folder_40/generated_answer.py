def filter_chars(s):
    chars_to_remove = [c for c in s[1:7] if '-' < c < 'L']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s