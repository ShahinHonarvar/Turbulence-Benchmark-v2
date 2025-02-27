def filter_chars(s):
    for i in range(86, 93):
        if i < len(s) and '!' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s