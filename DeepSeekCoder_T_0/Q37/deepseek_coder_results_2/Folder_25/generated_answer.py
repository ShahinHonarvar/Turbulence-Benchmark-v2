def filter_chars(s):
    for i in range(31, 39):
        if 31 <= i < len(s) and ';' <= s[i] <= 'g':
            s = s.replace(s[i], '')
    return s