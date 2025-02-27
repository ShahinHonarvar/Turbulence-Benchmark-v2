def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 54 <= i <= 83 and 'j' <= c <= 'v']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s