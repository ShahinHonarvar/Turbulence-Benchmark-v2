def filter_chars(s):
    for i in range(54, 92):
        if 'J' < s[i] < 'X':
            s = s.replace(s[i], '')
    return s