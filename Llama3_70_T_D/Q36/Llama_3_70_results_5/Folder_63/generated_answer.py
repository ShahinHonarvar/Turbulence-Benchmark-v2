def filter_chars(s):
    chars_to_remove = [c for c in s[26:80] if '<' < c < '>']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s