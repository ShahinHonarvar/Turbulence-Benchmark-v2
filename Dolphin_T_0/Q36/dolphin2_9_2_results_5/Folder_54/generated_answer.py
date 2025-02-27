def filter_chars(s):
    for i in range(18, 38):
        c = s[i]
        if c > ')' and c < 'P':
            s = s.replace(c, '')
    return s