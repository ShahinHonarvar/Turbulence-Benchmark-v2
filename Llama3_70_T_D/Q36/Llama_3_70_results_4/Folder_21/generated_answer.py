def filter_chars(s):
    chars_to_remove = [c for c in s[219:403] if '*' < c < '7']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s