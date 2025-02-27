def filter_chars(s):
    chars_to_remove = [c for c in s[34:68] if 'W' <= c <= 'x']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s