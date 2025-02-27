def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 37 <= i <= 56 and '6' <= c <= '_']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s