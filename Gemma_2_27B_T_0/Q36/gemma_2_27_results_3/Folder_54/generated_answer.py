def filter_chars(s):
    for i in range(18, 38):
        if s[i] > ')' and s[i] < 'P':
            s = s.replace(s[i], '')
    return s