def filter_chars(s):
    for i in range(1, len(s) - 1):
        if '8' < s[i] < 'm':
            s = s.replace(s[i], '')
    return s