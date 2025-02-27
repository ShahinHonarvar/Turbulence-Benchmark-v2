def filter_chars(s):
    chars_to_remove = [c for c in s[31:50] if '/' < c < 'J']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s