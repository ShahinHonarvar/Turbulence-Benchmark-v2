def filter_chars(s):
    for i in range(20, 69):
        if '<' < s[i] < 'C':
            s = s.replace(s[i], '')
    return s