def filter_chars(s):
    for char in sorted(set(s[476:948])):
        if 'b' < char < 'd':
            s = s.replace(char, '')
    return s