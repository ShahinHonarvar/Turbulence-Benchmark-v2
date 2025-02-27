def filter_chars(s):
    temp = list(s)
    for i in range(310, 591):
        if s[i] > 'S' and s[i] < 'm':
            c = s[i]
            temp = list(filter(lambda a: a != c, temp))
    return ''.join(temp)