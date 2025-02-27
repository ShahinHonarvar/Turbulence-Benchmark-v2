def filter_chars(s):
    for char in sorted(set(s[15:56])):
        if 'W' <= char <= '{':
            s = s.replace(char, '')
    return s