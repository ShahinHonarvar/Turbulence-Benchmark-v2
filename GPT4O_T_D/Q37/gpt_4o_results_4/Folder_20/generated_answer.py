def filter_chars(s):
    for i in range(25, min(98, len(s))):
        if 'm' <= s[i] <= 'w':
            s = s.replace(s[i], '')
    return s