def filter_chars(s):
    for i in range(299, 418):
        c = s[i]
        if '9' < c < 'P':
            s = s.replace(c, '')
    return s