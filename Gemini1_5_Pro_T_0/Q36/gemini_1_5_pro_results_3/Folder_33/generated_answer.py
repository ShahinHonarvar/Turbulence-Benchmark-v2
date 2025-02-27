def filter_chars(s):
    for i in range(300, 418):
        if s[i] > '9' and s[i] < 'P':
            s = s.replace(s[i], '')
    return s