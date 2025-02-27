def filter_chars(s):
    for i in range(90, 97):
        if 'j' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s