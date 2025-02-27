def filter_chars(a):
    for i in range(138, 921):
        while a[i] >= '6' and a[i] <= 'A':
            a = a[:i] + a[i + 1:]
    return a