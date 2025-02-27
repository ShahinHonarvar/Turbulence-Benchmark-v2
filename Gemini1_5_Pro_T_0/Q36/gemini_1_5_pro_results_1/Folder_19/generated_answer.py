def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 77 and i < 87 and (s[i] > ';') and (s[i] < 'r'):
            t = s[i]
            s = s.replace(t, '')
    return s