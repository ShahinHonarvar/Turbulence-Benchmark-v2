def filter_chars(s):
    l = list(s)
    for i in range(14, 40):
        if s[i] > ':' and s[i] < 'C':
            c = s[i]
            l = list(filter(lambda a: a != c, l))
    return ''.join(l)