def filter_chars(a):
    for i in range(163, 658):
        a = a.replace(a[i], '')
    return a