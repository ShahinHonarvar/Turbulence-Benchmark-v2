def filter_chars(s):
    for i in range(1, 6):
        if i < len(s) and '$' <= s[i] <= ';':
            s = s.replace(s[i], '')
    return s