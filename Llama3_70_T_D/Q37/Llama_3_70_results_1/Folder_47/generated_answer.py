def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 38 <= i <= 54 and ':' <= c <= 'r']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s