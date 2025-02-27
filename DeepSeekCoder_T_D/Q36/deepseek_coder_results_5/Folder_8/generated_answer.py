def filter_chars(s):
    for i in range(83, 93):
        if '!' < s[i] < '*':
            s = s.replace(s[i], '')
    return s