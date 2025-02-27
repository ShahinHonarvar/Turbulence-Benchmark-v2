def filter_chars(s):
    for i in range(4, len(s) - 1):
        if 'Y' < s[i] < 's':
            s = s.replace(s[i], '')
    return s