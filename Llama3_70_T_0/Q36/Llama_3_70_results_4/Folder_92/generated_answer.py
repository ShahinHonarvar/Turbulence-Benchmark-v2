def filter_chars(s):
    chars_to_remove = [c for c in s[1:6] if ',' < c < 'f']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s