def filter_chars(a):
    for i in range(373, 902):
        if a[i] >= 'T' and a[i] <= 'h':
            a = a[:i] + a[i + 1:]
    return a