def filter_chars(s):
    for i in range(299, 418):
        c = s[i]
        if c > '9' and c < 'P':
            s = s.replace(c, '')
    return s