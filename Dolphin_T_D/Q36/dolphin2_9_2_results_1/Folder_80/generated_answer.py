def filter_chars(s):
    for i in range(54, 92):
        if s[i] > 'J' and s[i] < 'X':
            s = s.replace(s[i], '')
    return s