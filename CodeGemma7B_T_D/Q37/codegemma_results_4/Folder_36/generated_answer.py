def filter_chars(a):
    for i in a[259:503]:
        if ',' <= i <= '3':
            a = a.replace(i, '')
    return a