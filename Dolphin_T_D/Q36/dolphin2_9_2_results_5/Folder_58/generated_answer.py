def filter_chars(s):
    chars_range = s[318:337]
    for char in chars_range:
        if 'B' < char < 'z':
            s = s.replace(char, '')
    return s