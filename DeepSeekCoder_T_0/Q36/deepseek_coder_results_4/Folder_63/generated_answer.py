def filter_chars(s):
    for i in range(26, 80):
        if '<' < s[i] < '>':
            s = s.replace(s[i], '')
    return s