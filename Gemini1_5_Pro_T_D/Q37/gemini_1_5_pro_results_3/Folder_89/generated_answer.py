def filter_chars(s):
    chars_to_remove = ''
    for i in range(11, 33):
        if i < len(s) and '!' <= s[i] <= '@':
            chars_to_remove += s[i]
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s