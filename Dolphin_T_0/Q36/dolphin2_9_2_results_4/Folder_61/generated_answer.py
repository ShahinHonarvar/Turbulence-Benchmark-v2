def filter_chars(s):
    chars_to_remove = [c for c in s[3:9] if '*' < c < 'E']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s