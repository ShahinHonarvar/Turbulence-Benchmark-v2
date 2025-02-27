def filter_chars(s):
    for i in range(91, 96):
        if 'j' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s