def filter_chars(s):
    for i in range(91, 97):
        if 'j' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s