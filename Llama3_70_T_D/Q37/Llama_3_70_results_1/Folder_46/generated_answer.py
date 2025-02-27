def filter_chars(s):
    chars_to_remove = [c for c in s[11:73] if 'i' <= c <= 'v']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s