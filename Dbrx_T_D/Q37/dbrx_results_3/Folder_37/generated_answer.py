def filter_chars(s):
    chars_to_remove = [c for c in s[17:63] if 'O' <= c <= '^']
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s