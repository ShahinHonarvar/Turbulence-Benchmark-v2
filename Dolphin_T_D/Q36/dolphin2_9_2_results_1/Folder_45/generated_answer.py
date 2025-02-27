def filter_chars(s):
    for i in range(81, 87):
        if '!' < s[i] < 's':
            s = s.replace(s[i], '')
    return s