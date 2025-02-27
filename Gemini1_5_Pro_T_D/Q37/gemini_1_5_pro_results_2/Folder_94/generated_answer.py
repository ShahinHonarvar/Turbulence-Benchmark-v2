def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if i >= 51 and i <= 96 and (s[i] >= 'X') and (s[i] <= 'p'):
            c = s[i]
            s = s.replace(c, '')
    return s