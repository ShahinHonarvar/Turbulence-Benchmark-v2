def filter_chars(s):
    for char in sorted(set(s[25:98])):
        if 'm' <= char <= 'w':
            s = s.replace(char, '')
    return s