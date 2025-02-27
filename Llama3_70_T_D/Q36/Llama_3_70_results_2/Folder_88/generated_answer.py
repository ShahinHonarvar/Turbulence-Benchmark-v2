def filter_chars(s):
    chars_to_remove = [c for c in s[78:81] if 'S' < c < '[']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s