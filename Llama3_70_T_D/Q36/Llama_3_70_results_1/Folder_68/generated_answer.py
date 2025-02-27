def filter_chars(s):
    chars_to_remove = [c for c in s[1:9] if '8' < c < 'm']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s