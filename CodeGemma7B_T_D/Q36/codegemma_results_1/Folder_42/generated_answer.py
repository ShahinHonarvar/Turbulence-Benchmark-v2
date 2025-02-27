def filter_chars(a):
    for i in range(42, 68):
        c = a[i]
        if c > 't' and c < 'x':
            a = a.replace(c, '')
    return a