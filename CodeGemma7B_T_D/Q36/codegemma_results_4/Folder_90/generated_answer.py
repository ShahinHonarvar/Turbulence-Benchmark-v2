def filter_chars(a):
    for i in range(344, 874):
        if a[i] > 'f' and a[i] < '~':
            a = a[:i] + a[i + 1:]
    return a