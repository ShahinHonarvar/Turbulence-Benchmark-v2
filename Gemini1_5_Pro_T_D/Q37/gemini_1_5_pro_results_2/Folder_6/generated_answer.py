def filter_chars(s):
    chars_to_remove = ''
    for i in range(13, 29):
        if i < len(s) and s[i] >= 'c' and (s[i] <= 'n'):
            chars_to_remove += s[i]
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s