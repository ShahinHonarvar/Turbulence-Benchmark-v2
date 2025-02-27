def filter_chars(s):
    chars_to_remove = [c for c in s[33:36] if '>' < c < 'A']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s