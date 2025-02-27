def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if (i > 42 and i < 68) and (s[i] > 't' and s[i] < 'x'):
            s = s.replace(s[i], '')
    return s