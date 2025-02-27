def filter_chars(s):
    for i in range(20, 70):
        if s[i] > '<' and s[i] < 'C':
            s = s.replace(s[i], '')
    return s