def filter_chars(s):
    for i in range(55, 92):
        if s[i] > 'J' and s[i] < 'X':
            s = s.replace(s[i], '')
    return s