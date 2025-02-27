def filter_chars(s):
    for i in range(70, 97):
        if 'V' < s[i] < 'j':
            s = s.replace(s[i], '')
    return s