def filter_chars(s):
    chars_to_remove = [c for c in s[318:337] if 'B' < c < 'z']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s