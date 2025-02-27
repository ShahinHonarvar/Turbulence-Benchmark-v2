def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[19:93]) if '8' <= c <= 'm']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s