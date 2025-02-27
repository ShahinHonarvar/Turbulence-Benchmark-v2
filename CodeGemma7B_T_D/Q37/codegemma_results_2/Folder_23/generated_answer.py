def filter_chars(a):
    for i in range(51, 78):
        if a[i] >= 'V' and a[i] <= 'Y':
            a = a[:i] + a[i + 1:]
    return a