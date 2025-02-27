def filter_chars(s):
    chars_to_remove = [c for c in s[154:222] if 'A' < c < 'f']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s