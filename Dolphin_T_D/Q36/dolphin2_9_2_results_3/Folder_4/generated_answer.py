def filter_chars(s):
    chars_to_remove = [c for c in s[42:67] if '6' < c < 'g']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s