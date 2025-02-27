def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 73 <= i <= 74 and 'U' <= c <= 'l']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s