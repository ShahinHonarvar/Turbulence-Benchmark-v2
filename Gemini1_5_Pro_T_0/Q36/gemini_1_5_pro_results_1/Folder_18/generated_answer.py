def filter_chars(s):
    l = list(s)
    for i in range(588, 648):
        if l[i] > ',' and l[i] < 'c':
            c = l[i]
            l = list(filter(lambda x: x != c, l))
    return ''.join(l)