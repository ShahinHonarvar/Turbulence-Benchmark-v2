def filter_chars(s):
    chars_to_remove = [c for c in s[19:69] if '<' < c < 'C']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s